from decimal import Decimal, getcontext
import decimal
import json
import subprocess
import pprint
import time
import sys

NON_WALLET_ADDRESSES = ["bcrt1qpaqttjj2kwy6u3yhf2kwskyemjcskhqfcnq5ax", "bcrt1qrrkk6e6zvcet46y0ehrlrzt6kgjx6vynrxhuht", "bcrt1qyvsuagaghhx03j07an9wuxqlqhug0tjsj8puy2",
  "bcrt1q8s576mzupz4twdykykpqrxav7j0yvj8yvxzs3p", "bcrt1qv0v5kxqupzz89e87qpkdcfx5hxdd7qtpqnyvsv", "bcrt1qwpp9nflnhl95ue4zncjludtqh9gf2hvvqzgjau",
  "bcrt1qk2c4nl7clqn60k768xv03vgpafp87gpak08ceu", "bcrt1qazkpa2yjvd4rrvl302c8qjmqccw5l4gw6wufyy", "bcrt1qa64u65xkk42xcn9fnw75ay79pn365q80zlasdm",
  "bcrt1qal483r47sdgs0ffgvgfvh54yux3c9rz2guys55"]
COINBASE_FEES_ADDRESS = "bcrt1qd8nnur2ef9vqcjz42emupejhglnune04uhunpf"

def arg_to_cli(arg):
    if isinstance(arg, bool):
        return str(arg).lower()
    elif arg is None:
        return 'null'
    elif isinstance(arg, dict) or isinstance(arg, list):
        return json.dumps(arg)
    else:
        return str(arg)

def send_cli(bitcoin_binary_path_with_wallet, clicommand=None, *args, **kwargs):
    """Run bitcoin-cli command. Deserializes returned string as python object."""
    pos_args = [arg_to_cli(arg) for arg in args]
    named_args = [str(key) + "=" + arg_to_cli(value) for (key, value) in kwargs.items()]
    
    p_args = bitcoin_binary_path_with_wallet.split(" ")
    if named_args:
        p_args += ["-named"]
    if clicommand is not None:
        p_args += [clicommand]
    p_args += pos_args + named_args
    # print("Running bitcoin-cli command: {}".format(" ".join(p_args)))

    process = subprocess.Popen(p_args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    cli_stdout, cli_stderr = process.communicate(input=None)
    returncode = process.poll()
    if returncode:
      print(cli_stdout, cli_stderr, returncode)
      raise subprocess.CalledProcessError(returncode, p_args, output=cli_stderr)
    
    try:
        if not cli_stdout.strip():
            return None
        return json.loads(cli_stdout, parse_float=Decimal)
    except (json.JSONDecodeError, decimal.InvalidOperation):
        return cli_stdout.rstrip("\n")

def generate_addresses(bitcoin_binary_path_with_wallet):
  for _ in range(0, 5000):
    new_address = send_cli(bitcoin_binary_path_with_wallet, "getnewaddress", "coinbase", "bech32")
    # pprint.pp(new_address)
    response = send_cli(bitcoin_binary_path_with_wallet, "generatetoaddress", 1, new_address)
    # pprint.pp(response)

    blockcount = send_cli(bitcoin_binary_path_with_wallet, "getblockcount")
    # pprint.pp(blockcount)

    time.sleep(0.01)

def spend_individual_unspent(bitcoin_binary_path_with_wallet, unspent):
  unspent_value = Decimal(unspent["amount"])
  receiving_same_wallet_address = send_cli(bitcoin_binary_path_with_wallet, "getnewaddress", "passthrough", "bech32")

  # round is done to avoid "Invalid Amount" error
  # 0.5% spread across non wallet addresses, +1 is done to account for fees that will be sent to the coinbase address in block generation
  non_wallet_address_amount = round((Decimal(0.005) * unspent_value) / (len(NON_WALLET_ADDRESSES) + 1), 8)
  # 99.5% back to the same wallet
  wallet_address_amount = round(Decimal(0.995) * unspent_value, 8)
  # print(unspent_value, wallet_address_amount, non_wallet_address_amount, (wallet_address_amount + (non_wallet_address_amount * len(NON_WALLET_ADDRESSES))))
  print("TxFee: ", unspent_value - (wallet_address_amount + (non_wallet_address_amount * len(NON_WALLET_ADDRESSES))))
  all_outputs = [{receiving_same_wallet_address: str(wallet_address_amount)}] + [{NON_WALLET_ADDRESSES[index]: str(non_wallet_address_amount)} for index in range(0, len(NON_WALLET_ADDRESSES))]
  
  # Create Tx
  unsigned_transaction = send_cli(bitcoin_binary_path_with_wallet, "createrawtransaction", [{"txid": unspent["txid"], "vout": unspent["vout"]}], all_outputs)
  # pprint.pp(unsigned_transaction)

  # Sign Tx
  signed_transaction = send_cli(bitcoin_binary_path_with_wallet, "signrawtransactionwithwallet", unsigned_transaction)
  # pprint.pp(signed_transaction)

  # Send Tx
  if signed_transaction["complete"] == True:
     # 0 to accept any feerate; maxfeerate=100000 > 10000 per KB
    send_response = send_cli(bitcoin_binary_path_with_wallet, "sendrawtransaction", signed_transaction["hex"], 0)
    pprint.pp(send_response)
  else:
    print("Tx not signed properly: ", signed_transaction)

def analyze_unspents(unspents):
  pos = 0; lessthanone = 0; neg = 0
  for i in range(0, len(unspents)):
    unspent = unspents[i]
    if unspent["amount"] >= 0.001:
      pos += 1
    elif unspent["amount"] < 0.001:
      lessthanone += 1
    elif unspent["amount"] < 0:
      neg += 1
  print(pos, lessthanone, neg, len(unspents))

def spend_unspents(bitcoin_binary_path_with_wallet, unspents_to_spend):
  unspents = send_cli(bitcoin_binary_path_with_wallet, "listunspent")
  # Spend largest unspents first to avoid hitting the "dust" amount error because of the non wallet address amounts being so low
  unspents.sort(key=lambda unspent: unspent["amount"], reverse=True)
  unspents = [unspent for unspent in unspents if unspent["amount"] > 0] # get unspents with some balance
  # analyze_unspents(unspents)
  unspents = unspents[:unspents_to_spend]
  for i in range(0, len(unspents)):
    spend_individual_unspent(bitcoin_binary_path_with_wallet, unspents[i])

def generate_blocks(bitcoin_binary_path_with_wallet, block_count):
  for i in range(0, block_count):
    # Put 10+1 transactions in every block
    spend_unspents(bitcoin_binary_path_with_wallet, 10)
    block_generated = send_cli(bitcoin_binary_path_with_wallet, "generatetoaddress", 1, COINBASE_FEES_ADDRESS)
    print(i, block_generated)

def main():
  bitcoin_binary_path_with_wallet = sys.argv[1]
  # Generate 1000 blocks each time the script is run
  # More blocks lead to more unspents generated due to coinbase outputs
  generate_blocks(bitcoin_binary_path_with_wallet, 1000)

if __name__ == "__main__":
    main()