## Musig2
* It's a n-of-n multi-signature scheme that is interactive and requires coordination
 among the signers. It's not a m-of-n scheme.
* Multiple signers come together to aggregate their keys to form a `PubKeyAgg`
 while generating the final public key.
 * Multiple signers come together to aggregate their partial signatures as well to
 form the final signature. Such aggregation is possible due to linearity of Schnorr
 Signatures.

## ScriptPath
* A 998-of-999 Taproot Script Spend Mainnet: https://mempool.space/tx/7393096d97bfee8660f4100ffd61874d62f9a65de9fb6acf740c4c386990ef73

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
