# Schnorr

## Terminology
```
c = challenge
r = secret nonce
R = public nonce
x = secret key
X = public key
m = message
σ = signature
```

### Sign
```
c = H(X, R, m)
s = x * c + r
σ = (R, s)
```

### Verify
```
g ^ s = g ^ (x * c + r)
g ^ s = (g ^ (x * c)) * (g ^ r)
g ^ s = (X ^ c) * R
```

* Challenge (c) is constructed using all the public elements X, R, m. So that 
 it can be recreated during the verification process.
* The `s` equation can be thought of being exponent-iated to the generator point
 (g) during the verification process.
* As seen, the verification process requires only the publicly known elements
 such as the generator point (g), s value of the signature, the public key (X),
 the challenge (c) that can be calculated using X|R|m, the public nonce (R).
* For a given X and m, signing again would lead to a new secret nonce (r), and
 hence a new R, and then a new s. Signing the same message using the same public
 key again would lead to a new signature!
