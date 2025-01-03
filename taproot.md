## Musig2


## ScriptPath
* Transaction Script Spend Mainnet: https://mempool.space/tx/7393096d97bfee8660f4100ffd    61874d62f9a65de9fb6acf740c4c386990ef73

* `OP_CHECKMULTISIG/OP_CHECKMULTISIGVERIFY` are disabled in TapScript due to being
 inefficient because there is an underlying 'polling' mechanism while verifying
 the multiple signatures. A signature is verified against `n` pubkeys in an m-n
 multisig setup.
* This is improved upon by `OP_CHECKSIGADD` that simply checks 1 signature against
 1 pubkey and increments the matched signature counter by 1 if the signature matched
 with the pubkey. At the end of the script, there's a `OP_NUMEQUAL` opcode that
 verifies the total matched signatures with a number preceding this opcode.

