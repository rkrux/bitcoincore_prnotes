## Sighash

* Depending upon the kind of transaction data signed, there are different ways
 signatures can be created for the inputs in the transaction.

 Type | Value | Meaning 
 ---- | ----- | ------- 
 SIGHASH_ALL | 01 | Sign all inputs and all outputs
 SIGHASH_NONE | 02 | Sign all inputs and no outputs
 SIGHASH_SINGLE | 03 | Sign all inputs and 1 corresponding output
 SIGHASH_ALL - SIGHASH_ANYONECANPAY | 81 | Sign only 1 input and all outputs
 SIGHASH_NONE - SIGHASH_ANYONECANPAY | 82 | Sign only 1 input and no outputs
 SIGHASH_SINGLE - SIGHASH_ANYONECANPAY | 83 | Sign only 1 input and 1 corresponding output
