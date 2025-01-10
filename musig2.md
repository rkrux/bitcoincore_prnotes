# Musig2 notes

* A 2-round protocol for aggregating public keys and partial signatures. Supports
 concurrent signing sessions, is non-interactive, outputs ordinary Schnorr sigs.

* Every signer must generate >= 2 secret nonces and the combined nonce for each
 signer is the sum of the nonces where each nonce after the first one is 
 exponentiated by `b`, where b is derived by a hash function applied on the
 nonces of all the signers.

* This ensures that the nonces of the signers are tied to each other. If an
 adversary changes the nonce, the nonce of the honest signers also changes, which
 ensures that the combined nonce of all signer also changes and is no longer 
 constant.

```
si = ki + ki' + e * ai * pi

where e = hash(R || P || m)
R = aggregated group nonce
P = aggregated group public key
ai = aggregation coefficient of the signer
```
