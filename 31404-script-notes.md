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
 `Segwit` script, which leads to custom handling in the script execution code.
 * P2WPKH: <OP_0> <OP_PUSHBYTES_20> <PUBKEY_HASH>
 	* Hex: <00><14><20bytes(40chars)-pubkeyhash>
	* The `scriptPubKey` length is 22 bytes / 44 chars.
 * P2WSH: <OP_0> <OP_PUSHBYTES_32> <SCRIPT_HASH>
 	* Hex: <00><20><32bytes(64chars)-scripthash>
	* The `scriptPubKey` length is 34 bytes / 68 chars.
 * The addresses start from `bc1q` and the length can be 42 or 62 chars. 
 * Uncompressed Public Keys are NOT allowed.

## Common script patterns
 * Upto 75 bytes can be pushed onto the stack starting from 1. Hex values: 01-4b
 	* In ASM, they are denoted by OP_PUSHBYTES_XX.
 * Usually, compressed pubkeys are expressed in 33 bytes: 1 byte (02 or 03) that
 denotes whether the y-coordinate is even or odd. That's why it's common to notice
 `OP_PUSHBYTES_33` in the "locking code".
 	* However, in Taproot, 32 bytes pubkeys are used because only the points
 with even coordinates are used, so there is no need to have an extra byte 
 denoting the y-coordinate parity.
	* In legacy scripts, uncompressed public keys were also used that were
 65 bytes in length expressed by both the X and Y coordinates (& 04 prefix). 
 They were more expensive to spend due to leading to larger transaction size.
 * `OP_HASH160` (& `OP_RIPEMD160`) returns a 160-bit (20 bytes) hash, that's why 
there'd be a `14` hex value succeeding it - `a914`. Common scripts using it are 
`P2PKH`, `P2SH`, `P2WPKH`.
 * `OP_SHA256` (& `OP_HASH256`) returns a 256-bit (32 bytes) hash, that's why a
 `20` hex value would be present after it - `a820` or `aa20`.

 Script | Hash Function (at Top level)
 ------ | -------------
 P2PK | None
 P2PKH | HASH160
 P2MS | None
 P2SH | HASH160
 P2WPKH | HASH160
 P2WSH | SHA256
 P2TR | None

### Common Opcodes

 Name | Decimal | Hex
 ---- | ------- | ---
 OP_0 | 00 | 00
 OP_PUSHBYTES_20 | 20 | 14
 OP_PUSHBYTES_32 | 32 | 20
 OP_PUSHBYTES_33 | 33 | 21
 OP_PUSHBYTES_65 | 65 | 41
 .. | .. | .. 
 OP_1 | 81 | 51
 OP_2 | 82 | 52
 OP_3 | 83 | 53
 OP_16 | 96 | 60
 .. | .. | ..
 OP_VERIFY | 105 | 69
 OP_RETURN | 106 | 6a
 .. | .. | ..
 OP_DUP | 118 | 76
 .. | .. | ..
 OP_EQUAL | 135 | 87
 .. | .. | ..
 OP_RIPEMD160 | 166 | a6
 OP_SHA256 | 168 | a8
 OP_HASH160 | 169 | a9
 OP_HASH256 | 170 | aa
 .. | .. | ..
 OP_CHECKSIG | 172 | ac
 OP_CHECKMULTISIG | 174 | ae

## Common limits/numbers:
 * 10,000 bytes for the witness script.
 * 100 stack items before the witness script in witness. 
 * 520 bytes limit each stack item.
 * 520 bytes limit for the redeemScript (much smaller than the witnessScript).
 * With the 520 byte limit, maximum 15 pubkeys can be used in the multi-sig 
   script nested inside the P2SH. More than 15 keys in the script is consensus
 invalid.

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
 * Note: The raw 32-byte public key is used, not its hash.
 * `OP_1` at the start signifies Taproot that requires custom handling, no need
 to manually add the script elements on the stack like done in P2PKH, P2SH.
 * The addresses start from `bc1p` and are 62 chars in length.

### KeyPath Spending
 * While spending from the `keypath`, a signature from a key is required. 
 Multiple keys can be used/aggregated to form the final single key this is 
 possible due to Schnorr Signatures and PubKey Aggregation. It is tweaked by the
 script commitment hash and then the signature from the final tweaked key goes 
 in the witness.
 * Since tweaking is required while "unlocking" the output, the script tree 
 needs to be stored and retrieved while spending from the `keypath` as well.
 * Only 1 item - a signature - is present in the `witness` field.
 * Witness: <KEY_SIGNATURE>

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
 * Witness: <SPENDING_SCRIPT_SIGS><SPENDING_SCRIPT><CONTROL_BLOCK:PUBKEY_AND_MERKLEPATH>

