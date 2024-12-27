# Key/Random notes on Bitcoin Script

- `scriptPubKey` is the way outputs are locked. Think of it as "locking code".
- `scriptSig` is the way outputs ("inputs" in tx context) are unlocked. Think of
it as "unlocking code".
- It's called `scriptPubKey` because initially the outputs were locked to the 
public key mostly and they were unlocked using the key signatures, that's why 
called `scriptSig`.
- Standard scripts involve locking using signatures/private/public keys directly
 or indirectly because adding the signature in the transaction doesn't reveal
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

## Segwit
 * `OP_0` at the start of the "locking script"/`scriptPubKey` signifies 
 `Segwit` script.
 * P2WPKH: <OP_0> <OP_PUSHBYTES_20> <PUBKEY_HASH>
 	* Hex: <00><14><20bytes(40chars)-pubkeyhash>
 * P2WSH: <OP_0> <OP_PUSHBYTES_32> <SCRIPT_HASH>
 	* Hex: <00><20><32bytes(64chars)-scripthash>

## Common script patterns

## Common limits/numbers:
 * 10,000 bytes for the witness script.
 * 100 stack items before the witness script in witness. 
 * 520 bytes limit each stack item.
 * 520 bytes limit for the redeemScript (much smaller than the witnessScript).
 * With the 520 byte limit, maximum 15 pubkeys can be used in the multi-sig 
   script nested inside the P2SH.

## Taproot
 * It is essentially a superset of P2WKH and P2WSH as in both the spending paths
 are possible within it - `key path` and `script path`.
 * The end pubkey that is used to generate the Taproot address is a `tweak` of 
 the public key of the `keypath` and the Merkle Root of the tree of the scripts
 used in the `scriptpath`.
 * `Tweaking` is the modulo addition of the pubkey from the `keypath` to the 
 script commitment hash from the `scriptpath`.
 * TweakedPublicKey ~ (KeyPathPublicKey + ScriptsTreeMerkleRoot) % N
 * `scriptPubKey`: <OP_1> <OP_PUSHBYTES_32> <TWEAKED_PUBLIC_KEY>
 * `OP_1` at the start signifies Taproot that requires custom handling, no need
 to manually add the script elements on the stack like done in P2PKH, P2SH.

### KeyPath Spending
 * While spending from the `keypath`, a signature from a key is required. 
 Multiple keys can be used/aggregated to form the final single key this is 
 possible due to Schnorr Signatures and PubKey Aggregation. It is tweaked by the
 script commitment hash and then the signature from the final tweaked key goes 
 in the witness.
 * Since tweaking is required while "unlocking" the output, the script tree 
 needs to be stored and retrieved while spending from the `keypath` as well.
 * Only 1 item - a signature - is present in the `witness` field.
 * {key-signature}

### ScriptPath Spending
 * In the `scriptpath`, there can be bunch of scripts from which any one can be 
 used to spend. The other scripts need not be revealed, thereby increasing 
 privacy. Only the hashes of the other scripts in the MerklePath need to be 
 revealed proving the presence of the spending script in the script tree.
 * 3 items are present in the `witness` field: spending script sigs, whole 
 spending script, control block: contains pubkey from the `keypath` and the 
 `MerklePath` of the spending script to prove the presence of the spending script
 in the script tree.
 * Note: The pubkey from the `keypath` is still required while spending from the
 `scriptpath`.
 * {spending-script-sigs}{spending-script}{control-block:pubkey-and-merklepath} 
