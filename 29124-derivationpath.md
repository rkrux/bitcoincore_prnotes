### Wallet Commands

Command | Description | Legacy Only
------- | ----------- | -----------
loadwallet | Loads a wallet from a wallet file or directory | No
unloadwallet | Unloads the wallet referenced by the request endpoint, otherwise unloads the wallet specified in the argument | No
dumpwallet | Dumps all wallet keys in a human-readable format to a server-side file. This does not allow overwriting existing files | Yes
restorewallet | Restores and loads a wallet from backup. The rescan is significantly faster if a descriptor wallet is restored | No
backupwallet | Safely copies the current wallet file to the specified destination | No
importwallet |  Imports keys from a wallet dump file (see dumpwallet). Requires a new wallet backup to include imported keys. | Yes
sethdseed | Set or generate a new HD wallet seed. Non-HD wallets will not be upgraded to being a HD wallet. | Yes
keypoolrefill | Fills the keypool | No 

* The seed value can be retrieved using the dumpwallet command. It is the 
private key marked hdseed=1.

### LegacyScriptPubKeyMan::DeriveNewChildKey()
* https://github.com/bitcoin/bitcoin/blob/28.x/src/wallet/scriptpubkeyman.cpp#L1129
* // we use a fixed keypath scheme of m/0'/0'/k
* // key at m/0'/0' (external) or m/0'/1' (internal)

### RestoreWallet Trace
wallet/rpc/backup.cpp | restorewallet()
wallet/wallet.cpp | RestoreWallet(), LoadWallet(), LoadWalletInternal(), CWallet::Create(), CWallet::LoadWallet()
wallet/walletdb.cpp | WalletBatch::LoadWallet(), LoadLegacyWalletRecords(), LoadRecords(), LoadRecords()

### Dump Wallet Format
* https://github.com/bitcoin/bitcoin/blob/28.x/src/wallet/rpc/backup.cpp#L778-L802

```
encodedSecretKey createdTime change/reserve/hdseed/inactivehdseed=1 # addr=<address> hdkeypath=m/0'/0'/k'
scriptPubKeyHex createdTime cscript=1 # addr=<address>
```

