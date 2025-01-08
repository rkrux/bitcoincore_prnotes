# Schnorr

## Terminology
```
c, e = challenge
r = secret nonce
R = public nonce
x, k = secret key
X = public key
m = message to be signed
s = signature
σ = (R, s) that's shared with the counterparty
G = generator point on the curve
```
- r is scalar, R is a point on the curve
- x or k is scalar, X is a point on the curve

### Sign
```
e = H(X || R || m)
s = r + k * e
σ = (R, s)
```

### Verify
```
G * s = G * (r + k * e)
G * s = G * r + ((G * k) * e)
G * s = R + (X * e)
```
- Verification involves multiplying the signature with the generator point and
 checking that it equals public nonce (R) plus public key (X) multiplied by the
 challenge (e).

-----

* Challenge (c or e) is constructed using all the public elements X, R, m. So that 
 it can be recreated during the verification process.
* The `s` equation can be thought of being multiplied to the generator point
 (G) during the verification process.
* As seen, the verification process requires only the publicly known elements
 such as the generator point (G), s value of the signature, the public key (X),
 the challenge (c, e) that can be calculated using H(X||R||m), the public nonce (R).
* For a given X and m, signing again would lead to a new secret nonce (r), and
 hence a new R, and then a new s. Signing the same message using the same public
 key again would lead to a new signature!
