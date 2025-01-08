# Schnorr

## Terminology
```
c, e = challenge
r = secret nonce
R = public nonce
x, k = secret key
X, P = public key
m = message to be signed
s = signature
σ = (R, s) that's shared with the counterparty
G = generator point on the curve
```
- r is scalar, R is a point on the curve
- x or k is scalar, X is a point on the curve

### Sign
```
k, r <- $
P = k * G
R = r * G

e = H(P || R || m)
s = r + k * e
σ = (R, s)
```

### Verify
```
G * s = G * (r + k * e)
G * s = G * r + ((G * k) * e)
G * s = R + (P * e)
```
- Verification involves multiplying the signature with the generator point and
 checking that it equals public nonce (R) plus public key (X, P) multiplied by the
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
-----

* The private key and the private nonce are scalar values.
* Once multiplied the generator point, they yield points on the curve that become
 the public key and the public nonce.
* Schnorr signatures are preferred because of their linaerity and additive 
 property. That's why they end up used in multi-signature algorithms such as
 MuSig. There is no division or inverse calculation required in Schnorr like needed
 in ECDSA signatures.
-----

### Why nonce is needed
* s and e are public.
* r and k are private.

```
s = r + k * e
(s - r) / e = k
```

```
s = k * e
s / e = k
```
* If r had not been there in the equation, then calculating the private key (k)
 from the signature becomes quite easy. It's only because of the private variable
 `r` that calculating the private key from the signature is not possible.

### Adding Schnorr signatures on same message (MultiSig)
```
P12 = P1 + P2
e = H(R1 || R2 || P1 || P2 || m)
s1 = r1 + k1 * e
s2 = r2 + k2 * e

s1 + s2 = r1 + k1 * e + r2 + k2 * e
s1 + s2 = (r1 + r2) + (k1 + k2) * e
s12 = r12 + k12 * e
```
* It's because of the linearity property that 2 signatures on the same message
 can be aggregated, and still yield the combined signature in the form 
 `r' + k' * e`.

### Key Cancellation Attack
* It's possible for a malicious user to choose their public key and nonce in
 such a way that cancels out the public key and the public nonce of the other
 user if the malicious user already knows them beforehand.

```
P1, R1
P2 = P2' - P1
R2 = R2' - R1
```
* User 1 is using P1 and R1 but the user 2 ends up using P2 and R2 values and
 communicate them to user 1. Both P2 and R2 subtracts P1 and R1 from their actual
 values (P2', R2') which they keep private.

**Public Key and Nonce**
```
P12 = P1 + P2 = P1 + P2' - P1 = P2'
R12 = R1 + R2 = R1 + R2' - R1 = R2'
```
* So P12 and R12 comes out to be the actual public key (P2') and nonce (R2') of
 user 2.

**Sign and Verify**
* User 2 doesn't have the private key for (P2), nor the secnonce for R2, but that
 need not matter, and they can create the combined signature themselves.
 
```
s1 = r1 + k1 * e
s2' = r2' + k2' * e [s2' is never made public]

s12 * G = R12 + P12 * e
 = (R1 + R2) + (P1 + P2) * e
 = (R1 + R2' - R1) + (P1 + P2' - P1) * e
s12 * G = R2' + P2' * e
s12 * G = (r2' + p2' * e) * G
s12 = r2' + p2' * e
s12 = s2'
```
* Since s12 equals s2', so the malicious user can send their own signature here!
* This attack is possible because of the linaerity of the Schnorr signatures.
* One way to mitigate this attack is to mandate for the user 2 to sign a message
 with the corresponding private key for P2, which they will not have. But this
 introduces one more step in the protocol and would need to be done for all the 
 signers involved in the aggregation model.
-----

### Sig Aggregation
* Another way to mitigate the key cancellation attack is to attach coefficients
 in the signature equation so that the keys of the honest user are not cancelled
 out.

**Sign**
```
si = ri + ki * ai * e
where 
si, ri, ki belong to the user i
ai = H(l || Xi)
l = H(X1 || ... Xn)
Xagg = sigma(ai * Xi) -> aggregate public key using linear combination
Rgg = sigma(Ri)

sagg = sigma(si)
```

**Verify**
```
sG = sigma(si) * G
 = sigma(ri + ki * ai * e) * G
 = sigma((ri * G) + (ki * ai * e * G))
 = sigma(Ri + (Xi * ai * e))
 = sigma(Ri) + sigma(Xi * ai * e)
 = Ragg + sigma(Xi * ai) * e
sG = Ragg + Xagg * e
```

**Key Cancellation Mitigation**
```
s12 * G = R12 + X12 * e
where X12 = a1 * X1 + a2 * X2 = a1 * X1 + a2 * (X2' - X1)
 and R12 = R1 + R2 = R1 + R2' - R1 = R2'

s12 * G = R2' + (a1 * X1 + a2 * (X2' - X1)) * e
 = r2' * G + (a1 * X1 + a2 * X2' - a2 * X1) * e
 = r2' * G + (a1 * G * k1 + a2 * G * k2' - a2 * G * k1) * e

(r2' + ks * e) * G = (r2' + (a1 * k1 + a2 * k2' - a2 * k1) * e) * G

Take off G, cancel out r2' on both sides, take off e on both sides

ks = r2' + a1 * k1 + a2 * k2' - a2 * k1
```

* This `ks` is the key that the malicious user needs to sign with. But this ks
 contains `k1` in the equation, which the malicious user (user 2) in this case 
 doesn't have. So the maluser can't be the only one signing now! 

### Replay Attack
* This technique is still prone to the replay attack i.e. if the same nonce is
 used to sign another message by the honest user. The malicious user can send out
 a new message for the honest user to sign but with the same nonce.
* The public keys remain same so `l` is same, and then `ai` is same.

```
si = ri + ai * ki * e
si' = ri + ai * ki * e'

si' - si = ri + ai * ki * e' - (ri + ai * ki * e)
si' - si = ri + ai * ki * e' - ri - ai * ki * e

ri cancels out in right side

si' - si = ai * ki * e' - ai * ki * e
(si' - si) / (ai * e' - ai * e) = ki
(si' - si) / ((e' - e) * ai) = ki
```
* `ki` can be found out just by subtracting the 2 signatures if the same nonce
is used. `si', si, e', e, ai` are public and known to the attacker.
* Imperative that once the nonce is used to come up with the partial signature,
 it must be obliterated so that the attacker can't use it again to sign any other
 message, otherwise the private key of the honest user would be leaked!

