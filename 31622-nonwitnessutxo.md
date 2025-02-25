### Why does non witness utxo need full previous transaction to be signed?

References:
1. https://bitcoin.stackexchange.com/questions/113782/segwit-includes-the-input-amount-in-the-signaturehash-what-possible-attack-can
2. https://bitcoinops.org/en/newsletters/2020/06/10/#fee-overpayment-attack-on-multi-input-segwit-transactions
3. https://github.com/bitcoin/bips/blob/master/bip-0143.mediawiki#motivation

Summary: To prevent fee overpayment attack on stateless signers.

The stateless signers such as hardware wallets don't have access to the full
blockchain and thus don't know the actual amount of the UTXO being spent by
the transaction. Therefore, they rely on external parties to provide them with
this data. A malicious external party can provide an incorrect UTXO value that
is being spent - usually understating the amount so that the fee calculated by
the signer is low, which the user will agree with. Underneath though, an UTXO
with a higher value is being spent leading to the user overpaying in the fees
unwillingly.

To combat this, for non-witness-utxos such signers require the full previous 
transaction details so that they can calculate the transaction id of that 
transaction themselves, and thus verifying the authenticity of the value of the
UTXO being spent.

For witness-utxos though, the hash digest, which will be signed by the signer and
later verified by the Bitcoin Core nodes, contains the amount value of the UTXO
being spent so that if an incorrect UTXO value has been passed by a malicious
party and later signed by the signer, the transaction containing this signature
will be rejected by the nodes. This was added in Segwit V0 transactions as part
of BIP 143.

Futhermore, signing only the value of the UTXO being spent leaves way for a
multi-segwit-input attack wherein the attacker makes the victim sign multiple
times leading to invalid signatures for each UTXO (and valid for the other ones).
The attacker can later combines all the valid signatures and broadcast this valid
transaction leading to over payment in the fees again! To counter this, the hash
digest algorithm makes the signer sign values of ALL the UTXOs being spent in the
transaction. This was added in Segwit V1 transactions as part of BIP 341.

> // non_witness_utxos can only be dropped if the sighash type does not include SIGHASH_ANYONECANPAY

Reference: https://github.com/bitcoin/bitcoin/blob/master/src/psbt.cpp#L448

Most likely because if ANYONECANPAY is used then the UTXO value of only the input
 being signed is committed to, more inputs can be added later in the transaction.
Due to the nature of ANYONECANPAY, there's special handling as to how the
 hashPrevouts and hashSequence are calculated while signing witness utxos.
