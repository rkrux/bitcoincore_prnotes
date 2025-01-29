# Notes on Segregated Witness (SegWit)

## Legacy Transaction Format
 1. `<nVersion> <txInsCount> <txIns> <txOutsCount> <txOuts> <nLockTime>`
 2. txIn - `<prevOutTx> <prevOutIndex> <scriptSig> <nSequence>`
 3. txOut - `<amount> <scriptPubKey>`

* The `txId` is the double sha256 (`HASH256`) of the transaction elements.
* Depending upon the `SIGHASH` type, different transaction elements are signed.
* But the `scriptSig` is not signed because the signature can't sign itself!
* The signatures can be malleated though through different ways such as using
 non-standard script elements like pushing and dropping elements, or by using 
 non-standard ways of pusing elements.
* This malleation doesn't invalidate the transaction because the signature is
 still valid.
* Since the `txId` is the hash of the data that includes the `scriptSig` as well,
 a malleated signature will lead to a new transactionId, which can be problematic
 for systems dependent on the immutability of the transacion id. Lightning Network
 particularly was affected by it.
* A malleated transaction is still valid and is very much possible to be confirmed
 instead of the original one.
* There were few rules specified in BIP62 to standardise the way signatures were
 created and the ways scripts were written.
* However, SegWit fixes the malleability issue in a more fundamental way.

## SegWit Transaction Format
 `<nVersion> <segwitMarker=00> <segwitFlag=01> <txInsCount> <txIns> <txOutsCount> <txOuts> <witness> <nLockTime>`

* The txIn and txOut formats remain the same.
* As seen and as evident in the name itsef, the `witness` is segregated from the
 input.
* This `witness` data is not used while coming up with the `txId`, and therefore
 any malleability in the `witness` section doesn't affect the `txId`.
* The `scriptSig` for witness inputs must be empty as per the specification, and
 therefore there can be no malleability in it.
* Interesingly, the `segwitMarker` was added at that particular position in the
 transaction so that the old non-upgraded nodes see the segwit transactions as
 having 0 inputs. Also, the the `flag` is `01` that is treated as the transaction
 having 1 output. A transaction with 0 input and 1 output if such a transaction
 is ever parsed by the old nodes but the segwit specific data (marker, flag, witness)
 are not sent to the old nodes because they never ask for it.
* The old un-upgraded nodes see a transaction spending segwit input as anyone can
 spend (ACS) and together will the lack of signatures on these inputs, these transactions
 are valid for old un-upgraded nodes as well. One of the reasons why funds should
 not be sent to addresses that are treated as anyone can spend because ANYONE 
 CAN indeed spend them.
* This should not be a concern for SegWit transactions though because prior to
 its activation majority of the nodes (and miners) would have upgraded and majority
 of the network would be rejecting such SegWit transactions if anyone did try to
 spend them.
* TODO: Where in the code is the Segwit input treated as ACS for old nodes?

### Brief on Scaling

* The witness data is discounted in the SegWit transactions by a factor of 4. The
 discount is reflected in the transaction size, and therefore in the transaction fees.
* A fully serialised transaction is represented in Bytes, which is sent over the
 wire.
* For block size calculation, a new unit `Weight Units` is used, which is calculated
 using `non-witness-data * 4 + witness-data` or `base-data-without-witness * 3 + full-tx-data`.
* This discounting incentivises the users in spending the inputs MORE. Otherwise,
 the users would keep on storing bitcoins in new UTXOs and not spend them enough.
* In absence of Segwit, besides reducing the spending activity on the network, it
  would also increase the UTXO set size & thereby discourage the users with lower
  system confs to run a bitcoin node.
* The `Weight Units` is the one that's used with the block size calculation of
 `4 million WUs`.
* Another unit introduced is `Virtual Bytes (vB)`, which is calculated using 
 `Weight Units (WU) / 4`.
