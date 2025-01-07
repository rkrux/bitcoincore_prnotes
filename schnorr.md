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
* The `s` equation can be thought of being exponent-iated to the generate point
 (g) during the verification process.
