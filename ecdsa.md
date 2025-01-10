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
