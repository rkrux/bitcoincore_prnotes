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
      - AttemptCoinSelection(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/spend.cpp#L791C32-L791C54
      - AttemptSelection(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/spend.cpp#L885
  - FinishTransaction(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L1296
  - CWallet::FillPSBT(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/wallet.cpp#L2181
  - FillPSBT(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L106
  - LegacyScriptPubKeyMan::FillPSBT(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/scriptpubkeyman.cpp#L634
  - SignPSBTInput(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/scriptpubkeyman.cpp#L661

This is where all the coin selection algorithms are executed and the best one is chosen based on the waste metric
  - ChooseSelectionResult: https://github.com/bitcoin/bitcoin/blob/master/src/wallet/spend.cpp#L685
    - max_input_weight deduction: https://github.com/bitcoin/bitcoin/blob/master/src/wallet/spend.cpp#L699
  - SelectCoinsBnB: https://github.com/bitcoin/bitcoin/blob/master/src/wallet/coinselection.cpp#L93C31-L93C45
  - BnB honouring max_weight argument: https://github.com/bitcoin/bitcoin/blob/master/src/wallet/coinselection.cpp#L190

All CoinSelection algorithms honour the max_weight criteria in case of automatic coin selection:
1. https://github.com/bitcoin/bitcoin/blob/master/src/wallet/coinselection.cpp#L190
2. https://github.com/bitcoin/bitcoin/blob/master/src/wallet/coinselection.cpp#L325
3. https://github.com/bitcoin/bitcoin/blob/master/src/wallet/coinselection.cpp#L538
4. https://github.com/bitcoin/bitcoin/blob/master/src/wallet/coinselection.cpp#L651
