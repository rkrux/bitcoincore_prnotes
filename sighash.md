## Sighash

* Depending upon the kind of transaction data signed, there are different ways
 signatures can be created for the inputs in the transaction.
* The data inside the Sighash once signed by any signer will be verified by the 
 nodes when the transaction is received or found in a block.
* Essentially signing any transaction data means finalising the data in the
 transaction. It can't be changed anymore if the transaction needs to be mined.
* The corresponding output below means the output with the same index as the
 input.
* The `SIGHASH_TYPE` is appended at the end of the DER encoded signatures in the
 transaction.
* Every input can have a different `SIGHASH_TYPE` in its signature.
* A `SIGHASH_NONE` type expects another input to have a `SIGHASH_ALL` type in its
 signature. Otherwise if no outputs are signed by any of the input signatures, the
 miner can simply change the output upon noticing this kind of transaction.

 Type | Value | Meaning 
 ---- | ----- | ------- 
 SIGHASH_ALL | 01 | Sign all inputs and all outputs
 SIGHASH_NONE | 02 | Sign all inputs and no outputs
 SIGHASH_SINGLE | 03 | Sign all inputs and 1 corresponding output
 SIGHASH_ALL - SIGHASH_ANYONECANPAY | 81 | Sign only 1 input and all outputs
 SIGHASH_NONE - SIGHASH_ANYONECANPAY | 82 | Sign only 1 input and no outputs
 SIGHASH_SINGLE - SIGHASH_ANYONECANPAY | 83 | Sign only 1 input and 1 corresponding output

 Type | Signer POV
 ---- | ----------
 SIGHASH_ALL | I'm finalising the transaction, no more inputs/outputs can be added 
 SIGHASH_NONE | I don't care where my funds go as long as others are also spending
 SIGHASH_SINGLE | I don't care where rest of the funds go as long as this recipient receives a certain amount
 SIGHASH_ALL - SIGHASH_ANYONECANPAY | I don't care who else funds the transaction as long as certain recipients recieve certain amounts
 SIGHASH_NONE - SIGHASH_ANYONECANPAY | Neither do I care who receives the funds, nor do I care who else contributes in the transaction; can be thought of as burning my funds or proving ownership of the funds.
 SIGHASH_SINGLE - SIGHASH_ANYONECANPAY | I don't care who else funds the transaction as long as this recipient receives a certain amount.

* `SIGHASH_ANYONECANPAY` can be used for **Crowdfunding** purposes. The first donator
 adds one input with `SIGHASH_ANYONECANPAY | SIGHASH_ALL` signifying no new outputs
 can be added. `SIGHASH_ALL` in this case is useful so that no one else ends up
 adding an output - maybe for compliance or legal purposes.
* `SIGHASH_NONE` can be thought of as creating a **Blank Cheque** where the spender
 just adds the input and doesn't care who the recipients are. If the miner sees
 such a transaction, then they would simply pay themselves by adding an output.
 Whosoever wants to receive funds in this transaction must use `SIGHASH_ALL` so
 that they ensure no one else can tamper with the transaction recipients. And if
 they have to use `SIGHASH_ALL`, that means they must add an input in the transaction.

### SIGHASH_SINGLE Bug
* Interestingly, for the `SIGHASH_SINGLE` type, if there is no corresponding output,
 then the software is programmed to consider signing the integer 1 here:
 https://github.com/bitcoin/bitcoin/blob/28.x/src/script/interpreter.cpp#L1618-L1624
* If somehow the signature of the integer `1` from the private key is available
 in public, then an attacker can create a transaction that has more inputs than
 the outputs. For all those inputs that don't have a corresponding output, the
 attacker can add the publicly available signature with the sighash type
 `SIGHASH_SINGLE`. The core software in nodes will be able to verify such
 transactions, and they can get mined!
* Remedy: Core doesn't sign such transactions where there is no corresponding
 output for the inputs in case of `SIGHASH_SINGLE` type:
 https://github.com/bitcoin/bitcoin/blob/28.x/src/script/sign.cpp#L823-L826. But
 other wallet softwares still can!
* Taproot specification doesn't allow signing such transactions as well:
 https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki?plain=1#L95

#### Reference transaction on mainnet
 * https://mempool.space/tx/791fe035d312dcf9196b48649a5c9a027198f623c0a5f5bd4cc311b8864dd0cf
 * There are 3 inputs and 1 output.
 * The last 2 inputs are multisig 2 of 3.
 * Notice the presence of `03 (SIGHASH_SINGLE)` at the end of 4 signatures of 
 the last 2 inputs - 2 signatures for 2 inputs each.
