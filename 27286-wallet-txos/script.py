import decimal
import json
import subprocess
import pprint
import time
import sys

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
    print("Running bitcoin-cli command: {}".format(" ".join(p_args)))

    process = subprocess.Popen(p_args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    cli_stdout, cli_stderr = process.communicate(input=None)
    returncode = process.poll()
    if returncode:
      print(cli_stdout, cli_stderr, returncode)
      raise subprocess.CalledProcessError(returncode, p_args, output=cli_stderr)
    
    try:
        if not cli_stdout.strip():
            return None
        return json.loads(cli_stdout, parse_float=decimal.Decimal)
    except (json.JSONDecodeError, decimal.InvalidOperation):
        return cli_stdout.rstrip("\n")

def generate_addresses(bitcoin_binary_path_with_wallet):
  for _ in range(0, 5000):
    new_address = send_cli(bitcoin_binary_path_with_wallet, "getnewaddress", "coinbase", "bech32")
    pprint.pp(new_address)
    response = send_cli(bitcoin_binary_path_with_wallet, "generatetoaddress", 1, new_address)
    pprint.pp(response)

    blockcount = send_cli(bitcoin_binary_path_with_wallet, "getblockcount")
    pprint.pp(blockcount)

    time.sleep(0.01)

def main():
  bitcoin_binary_path_with_wallet = sys.argv[1]
  # generate_addresses(bitcoin_binary_path_with_wallet)
  print("create, sign, send transactions")

if __name__ == "__main__":
    main()