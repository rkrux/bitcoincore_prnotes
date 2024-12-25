### Key/Random notes on Bitcoin Script

- `scriptPubKey` is the way outputs are locked. Think of it as "locking code".
- `scriptSig` is the way outputs ("inputs" in tx context) are unlocked. Think of
it as "unlocking code".
- It's called `scriptPubKey` because initially the outputs were locked to the 
public key mostly and they were unlocked using the key signatures, that's why 
called `scriptSig`.
- Standard scripts involve locking using signatures/private/public keys directly
 or indirectly because by adding the signature in the transaction doesn't reveal
 the private keys to the world.
- Non standard scripts can involve locking outputs without signatures but once
the scriptSig/witness data is revealed while spending the transaction, it can't/
shouldn't be reused because all the "private" data is revealed to the outside 
world.

- `witness` field is the way newer outputs are unlocked. `scriptSig` is for the
legacy ones.
- Legacy Scripts: P2PK, P2PKH, P2MS, P2SH.
- Newer Scripts: P2WPKH, P2WSH, P2TR.
- `witness` field is cost-discounted and thus incur lower costs while spending
in a transaction compared to the legacy scripts.

- Usually the pattern is to reduce the size of the locking script so that the 
sender doesn't incur the cost in the transaction while sending the funds to the 
recipient. That's why it's common to see hashes of stuff(keys/scripts) present 
in the locking code.
- And subsequently, it makes sense for the receiver to pay for the script cost 
when they spend those outputs in future transactions. That's why it's common to 
see the unlocking code to have all the spending data - multiple signatures, full
`witnessScript` or `redeemScript`, control block (in case of Taproot).
