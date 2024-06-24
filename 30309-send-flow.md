`send()` RPC builds, signs, and sends the transaction: https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L1187

Major subparts to it are:
  1. Fee Estimation: https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L1274
  2. RBF Deduction: https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L1278
  3. CreateRecipients(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L1281
  4. ConstructTransaction(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L1285
  5. SetOptionsInputWeights(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L1290
  6. FundTransaction(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L1294
      1. FundTransaction(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L707
      2. FundTransaction: https://github.com/bitcoin/bitcoin/blob/master/src/wallet/spend.cpp#L1391
      3. CreateTransaction(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/spend.cpp#L1337 
      4. CreateTransactionInternal(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/spend.cpp#L979
      5. SelectCoins: https://github.com/bitcoin/bitcoin/blob/master/src/wallet/spend.cpp#L1134
      6. SelectCoins(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/spend.cpp#L761 -> This is where the new condition is added.
      7. AttemptCoinSelection(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/spend.cpp#L791C32-L791C54
      8. AttemptSelection(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/spend.cpp#L885
  7. FinishTransaction(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L1296
  8. CWallet::FillPSBT(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/wallet.cpp#L2181
  9. FillPSBT(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/rpc/spend.cpp#L106
  10. LegacyScriptPubKeyMan::FillPSBT(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/scriptpubkeyman.cpp#L634
  11. SignPSBTInput(): https://github.com/bitcoin/bitcoin/blob/master/src/wallet/scriptpubkeyman.cpp#L661

This is where all the coin selection algorithms are executed and the best one is chosen based on the waste metric
  1. ChooseSelectionResult: https://github.com/bitcoin/bitcoin/blob/master/src/wallet/spend.cpp#L685
       1. max_input_weight deduction: https://github.com/bitcoin/bitcoin/blob/master/src/wallet/spend.cpp#L699
  3. SelectCoinsBnB: https://github.com/bitcoin/bitcoin/blob/master/src/wallet/coinselection.cpp#L93C31-L93C45
  4. BnB honouring max_weight argument: https://github.com/bitcoin/bitcoin/blob/master/src/wallet/coinselection.cpp#L190


### All CoinSelection algorithms honour the max_weight criteria in case of automatic coin selection:
1. https://github.com/bitcoin/bitcoin/blob/master/src/wallet/coinselection.cpp#L190
2. https://github.com/bitcoin/bitcoin/blob/master/src/wallet/coinselection.cpp#L325
3. https://github.com/bitcoin/bitcoin/blob/master/src/wallet/coinselection.cpp#L538
4. https://github.com/bitcoin/bitcoin/blob/master/src/wallet/coinselection.cpp#L651
