### Load/Unload/Dump/Restore/Backup/Import Wallet

Command | Description | Legacy Only
------- | ----------- | -----------
loadwallet | Loads a wallet from a wallet file or directory | No
unloadwallet | Unloads the wallet referenced by the request endpoint, otherwise unloads the wallet specified in the argument | No
dumpwallet | Dumps all wallet keys in a human-readable format to a server-side file. This does not allow overwriting existing files | Yes
restorewallet | Restores and loads a wallet from backup. The rescan is significantly faster if a descriptor wallet is restored | No
backupwallet | Safely copies the current wallet file to the specified destination | No
importwallet |  Imports keys from a wallet dump file (see dumpwallet). Requires a new wallet backup to include imported keys. | Yes

