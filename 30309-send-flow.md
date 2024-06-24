`send()` RPC builds, signs, and sends the transaction: https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L1187

Major subparts to it are:
  - Fee Estimation: https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L1274
  - RBF Deduction: https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L1278
  - CreateRecipients(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L1281
  - ConstructTransaction(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L1285
  - SetOptionsInputWeights(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L1290
  - FundTransaction(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L1294
      - FundTransaction(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L707
      - FundTransaction: https://github.com/bitcoin/bitcoin/blob/master/src/wallet/spend.cpp#L1391
      - CreateTransaction(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/spend.cpp#L1337 
      - CreateTransactionInternal(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/spend.cpp#L979
      - SelectCoins: https://github.com/bitcoin/bitcoin/blob/master/src/wallet/spend.cpp#L1134
      - SelectCoins(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/spend.cpp#L761 -> This is where the new condition is added.
  - FinishTransaction(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L1296
  - CWallet::FillPSBT(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/wallet.cpp#L2181
  - FillPSBT(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L106
  - LegacyScriptPubKeyMan::FillPSBT(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/scriptpubkeyman.cpp#L634
  - SignPSBTInput(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/scriptpubkeyman.cpp#L661
