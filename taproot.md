## Musig2
* It's a n-of-n multi-signature scheme that is interactive and requires coordination
 among the signers. It's not a m-of-n scheme.
* Multiple signers come together to aggregate their keys to form a `PubKeyAgg`
 while generating the final public key.
 * Multiple signers come together to aggregate their partial signatures as well to
 form the final signature. Such aggregation is possible due to linearity of Schnorr
 Signatures.

## ScriptPath

### A 998-of-999 Taproot Script Spend
 * On mainnet: https://mempool.space/tx/7393096d97bfee8660f4100ffd61874d62f9a65de9fb6acf740c4c386990ef73
 * The whole transaction is ~99KB in size.
 * The script path contains just 1 script, and no tree. Evident by the
 lack of Merkle Path in control block (will come later).
 * The spending script is of the format:
 `OP_PUSHBYTES_32 32_BYTES_PUBKEY OP_CHECKSIG OP_PUSHBYTES_32 32_BYTES_PUBKEY 
 OP_CHECKSIGADD OP_PUSHBYTES_32 32_BYTES_PUBKEY OP_CHECKSIGADD ...999times...
 e603 OP_GREATERTHANPREQUAL`.
 * `e603` is `998` in hex little endian format.
 * The spending script means that 998 signatures out of a total 999 public keys
 are required. It achieved multi-sig functionality in Tapscript with `CHECKSIGADD`. 
 * The witness contains 1001 items in total.
 * There are 998 valid signatures first, and then an invalid signature. Technically,
 the last 998 keys have provided valid signatures but in this case all the pubkeys
 are same.
 * So the first 999 items in the witness are the signatures.
 * Then is the full spending scrip in hex.
 * Then comes the Control Block with the control version (c1) and the internal
 public key of 32 bytes.
 * **Note**: The Sigops for this transaction is 0! Because the sig opcodes in the
 Tapscript are not included in the total block sigops limit. 

- - - -

* `OP_CHECKMULTISIG/OP_CHECKMULTISIGVERIFY` are disabled in TapScript due to being
 inefficient because there is an underlying 'polling' mechanism while verifying
 the multiple signatures. A signature is verified against `n` pubkeys in an m-n
 multisig setup.
* This is improved upon by `OP_CHECKSIGADD` that simply checks 1 signature against
 1 pubkey and increments the matched signature counter by 1 if the signature matched
 with the pubkey. At the end of the script, there's a `OP_NUMEQUAL` opcode that
 verifies the total matched signatures with a number preceding this opcode.
* The signatures in the witness for a script with `OP_CHECKSIGADD` come in the
 reverse order. For a `KEY1 KEY2 KEY3` kind of script, the signatures would appear
 in the order `SIG3 SIG2 SIG1`. A key that is not signing shall have an empty sig.

Few ways to achieve m-of-n functionality of `OP_CHECKMULTISIG` in Taproot:
1. Use a `PUBKEY1 OP_CHECKSIG PUBKEY2 OP_CHECKSIGADD M OP_NUMEQUAL` script.
2. Use a script tree of n `m-of-m` MuSig aggregated keys scripts.
3. Use a script tree of n `m-of-m` scripts such as 
 `PUBKEY1 OP_CHECKSIGVERIFY PUBKEY2 OP_CHECKSIG`.
