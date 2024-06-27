https://github.com/bitcoin/bitcoin/blob/master/src/wallet/spend.cpp#L137

`CalculateMaximumSignedTxSize()` is the function that estimates the size of the transaction assuming it's signed.
Internally it uses `GetSerializeSize()` for transaction outputs though.
