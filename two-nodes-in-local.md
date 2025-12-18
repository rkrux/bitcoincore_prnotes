### /tmp/node1/bitcoin.conf
```
  regtest=1
  [regtest]
  rpcport=18001
  rpcuser=test
  rpcpassword=test
  bind=127.0.0.1:18344 # added in the connect field of the other node
  bind=127.0.0.1:18345=onion
```

### /tmp/node2/bitcoin.conf
```
  regtest=1
  [regtest]
  rpcport=19001
  rpcuser=test
  rpcpassword=test
  bind=127.0.0.1:19344
  bind=127.0.0.1:19345=onion
  connect=127.0.0.1:18344
```

### bitcoind, bitcoin-cli
```
➜  doc git:(rpc_getorphantxs) ✗ currentbitcoind
bitcoind -datadir=/tmp/node1 -conf=/tmp/node1/bitcoin.conf -port=18000
bitcoind -datadir=/tmp/node2 -conf=/tmp/node2/bitcoin.conf -port=19000

bitcoincli -conf=/tmp/node1/bitcoin.conf getblockchaininfo
bitcoincli -conf=/tmp/node2/bitcoin.conf getblockchaininfo
```
