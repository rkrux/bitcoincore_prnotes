# ECDSA

```
R = s(hG + rP)

r = the x value of the point R
P = public key of the signer
h = hash of the transaction message
s = a scalar value that's the signature to be shared
```

* The equation is a discrete log relationship between a point R on the curve
and point that is the sum of the hash of the message multiplied by the Generator
 & the public key multiplied by a pseudorandom value that signer doesn't control.

* It's prone to malleability attacks because of the way the modulo inverse of s
is also a valid signature.

* 2 scalar multiplications are required in the equation compared to only 1 in
 Schnorr.

* More expensive computation due to the calculation of modular inverse while
 calculating `s`.

* The intuition behind coming up with this equation is that the prover/signer
 needs to prove to the verifier that they know the scalar `p` for the point `P`
 without sharing it directly, and the "additive shift" is included in the equation
 so that the verifier can't deduce the scalar for R `k` and the scalar for P `p`
 themselves.

* If the prover knows the discrete logs for `P` and `R`, then they come up with
 an `s` that is `R = s(hG + rP)`. The very equation here lets the verifier verify
 that the signer knows `p` but without revealing it.

