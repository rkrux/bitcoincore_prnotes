# Notes on Segregated Witness (SegWit)

## Transaction Format
 <nVersion> <txInsCount> <txIns> <txOutsCount> <txOuts> <nLockTime>

txIn - <prevOutTx> <prevOutIndex> <scriptSig> <nSequence>
txOut - <amount> <scriptPubKey>

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
 <nVersion> <segwitMarker> <segwitFlag> <txInsCount> <txIns> <txOutsCount> <txOuts> <witness> <nLockTime>

* The txIn and txOut formats remain the same.
* As seen and as evident in the name itsef, the `witness` is segregated from the
 input.
* This `witness` data is not used while coming up with the `txId`.
