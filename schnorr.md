# Schnorr

### Sign
```
c = H(X, R, m)
s = x * c + r
σ = (R, s)
```

### Verify
```
g ^ s = (X ^ c) * R
```

