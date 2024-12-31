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

 ### Scripts Hash functions
 Script | Hash Function (at Top level)
 ------ | -------------
 P2PK | None
 P2PKH | HASH160
 P2MS | None
 P2SH | HASH160
 P2WPKH | HASH160
 P2WSH | SHA256
 P2TR | None

 ### Commonly used Opcodes
 Name | Decimal | Hex
 ---- | ------- | ---
 OP_0 | 00 | 00
 OP_PUSHBYTES_20 | 20 | 14
 OP_PUSHBYTES_32 | 32 | 20
 OP_PUSHBYTES_33 | 33 | 21
 OP_PUSHBYTES_64 | 64 | 40
 OP_PUSHBYTES_65 | 65 | 41
 OP_PUSHBYTES_71 | 71 | 47
 OP_PUSHBYTES_72 | 72 | 48
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
 OP_EQUALVERIFY | 136 | 88
 .. | .. | ..
 OP_RIPEMD160 | 166 | a6
 OP_SHA256 | 168 | a8
 OP_HASH160 | 169 | a9
 OP_HASH256 | 170 | aa
 .. | .. | ..
 OP_CHECKSIG | 172 | ac
 OP_CHECKMULTISIG | 174 | ae

 ### Script Locking Unlocking Mental Models
 Script | Locking Model | Unlocking Model | Notes 
 ------ | ------------- | --------------- | -----
 P2PK | 1 pubkey | 1 sig by privkey | Just the sig is need that will be verified
 P2PKH | 1 pubkey hash | 1 sig by privkey, 1 pubkey | Along with sig, pubkey is required because it's needed to verify the sig of the privkey    
 P2MS | 1 script | N script-inputs | Only the required private key sigs are required for the multi-sig operator
 P2SH | 1 script hash | N script-inputs, 1 script hex | Original script hex (redeemScript) is required to verify the sigs because non-spending nodes don't have the script, OP_DUP is not needed because it's treated as a special case and the `redeemScript` is duplicated during stack execution 
 P2WPKH | 1 pubkey hash | 1 sig by privkey, 1 pubkey but in `witness` | Same as P2PKH but in `witness`
 P2WSH | 1 script hash | N script-inputs, 1 script hex but in `witness` | Same as P2SH but in `witness`
 P2TR - KeyPath | 1 tweaked pubkey | 1 sig by the `tweaked` privkey | Only the sig from the tweaked private key is enough, proves that the spender has both the internal private key and the MerkleHash of the scripts tree. Since the locking script indeed contains the pubkey (and not the hash), it's not required to add it again in the `witness`
 P2TR - ScriptPath | 1 tweaked pubkey | N script-inputs, 1 script hex, control-block:1 internal pubkey, merkle-path | Script inputs (data) and the spending script hex are used to indeed execute the spending script. The control block is used to prove that the spending script is part of the script tree. Adding the merke-path insead of only a signature by the tweaked public key because it's more thorough and completely proves where the spending script lies in the script tree. 

 ### Script Locking ASM/Hex
 Script | Common Locking ASM | Common Locking Hex
 ------ | ------------------ | ------------------
 P2PK | OP_PUSHBYTES_33 33_BYTES_PUBKEY OP_CHECKSIG | 21<66-chars>ac
 P2PKH | OP_DUP OP_HASH160 OP_PUSHBYTES_20 20_BYTES_PUBKEYHASH OP_EQUALVERIFY OP_CHECKSIG | 76a914<40-chars>88ac
 P2MS | OP_1 OP_PUSHBYTES_33 33_BYTES_PUBKEY1 OP_PUSHBYTES_33 33_BYTES_PUBKEY2 OP_2 OP_CHECKMULTISIG | 5121<66-chars>21<66-chars>52ae
 P2SH | OP_HASH160 OP_PUSHBYTES_20 20_BYTES_SCRIPTHASH OP_EQUAL | a914<40-chars>87
 P2WPKH | OP_0 OP_PUSHBYTES_20 20_BYTES_PUBKEYHASH | 0014<40-chars>
 P2WSH | OP_0 OP_PUSHBYTES_32 32_BYTES_SCRIPTHASH | 0020<64-chars>
 P2TR | OP_1 OP_PUSHBYTES_32 32_BYTES_TWEAKED_PUBKEY | 5120<64-chars>

 ### Script Unlocking ASM/Hex
 Script | Common Unlocking ASM | Common Unlocking Hex
 ------ | -------------------- | --------------------
 P2PK | OP_PUSHBYTES_72 72_BYTES_SIG | 48<144-chars>
 P2PKH | OP_PUSHBYTES_72 72_BYTES_SIG OP_PUSHBYTES_33 33_BYTES_PUBKEY | 48<144-chars>21<66-chars>
 P2MS | OP_0 OP_PUSHBYTES_72 72_BYTES_SIG | 0048<144-chars>
 P2SH | OP_0 OP_PUSHBYTES_72 72_BYTES_SIG OP_PUSHBYTES_XX XX_BYTES_SCRIPT | 0048<144-chars><XX-in-hex><XX*2-chars>
 P2WPKH | O2 OP_PUSHBYTES_72 72_BYTES_SIG OP_PUSHBYTES_33 33_BYTES_PUBKEY | 0248<144-chars>21<66-chars
 P2WSH | 03 OP_0 OP_PUSHBYTES_72 72_BYTES_SIG OP_PUSHBYTES_XX XX_BYTES_SCRIPT | 030048<144-chars><XX-in-hex><XX*2-chars>
 P2TR - KeyPath | O1 OP_PUSHBYTES_65 65_BYTES_SIG | 0141<130-chars>
 P2TR - ScriptPath | O3 #TODO: Add P2TR witness here

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
 * Taproot uses Schnorr Signatures, which are shorter than the ECDSA signatures.
 They are usually 64-65 bytes long compared to 71-72 bytes ECDSA ones.
 * In the `witness` section, just like for the `segwit` outputs, a witness items
 count is pushed first signifying the following witness items count - 1 for
 `KeyPath` spend & 3 or more for `ScriptPath` spend.
 * `OP_CHECKMULTISIG` is disabled in TapScript.
 * Merkle Path is the string concatenation of the leaf and branch hashes. The
 path length is limited to 128 such hashes. The longer the Merkle Path, the 
 larger is the unlocking script. Thus, more the transaction size and absolute fees.
 * It's recommended to put the commonly used script nearer to the root of the 
 tree, so that the Merkle Path is shorter, and hence lower fees.

### KeyPath Spending
 * While spending from the `keypath`, a signature from a key is required. 
 Multiple keys can be used/aggregated to form the final single key - this is 
 possible due to Schnorr Signatures and PubKey Aggregation. It is tweaked by the
 script commitment hash and then the signature from the final tweaked key goes 
 in the witness.
 * Since tweaking is required while "unlocking" the output, the script tree 
 needs to be stored and retrieved while spending from the `keypath` as well.
 * Only 1 item - a signature - is present in the `witness` field.
 * Witness: `<KEY_SIGNATURE>`

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
 * Witness: `<SPENDING_SCRIPT_SIGS><SPENDING_SCRIPT><CONTROL_BLOCK:CONTROL_VERSION_AND_PUBKEY_AND_MERKLEPATH>`

