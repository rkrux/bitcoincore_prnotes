### /tmp/node1/bitcoin.conf
```
  1 regtest=1
  2 [regtest]
  3 rpcport=18001
  4 rpcuser=test
  5 rpcpassword=test
  6 bind=127.0.0.1:18344 # added in the connect field of the other node
  7 bind=127.0.0.1:18345=onion
```

### /tmp/node2/bitcoin.conf
```
  1 regtest=1
  2 [regtest]
  3 rpcport=19001
  4 rpcuser=test
  5 rpcpassword=test
  6 bind=127.0.0.1:19344
  7 bind=127.0.0.1:19345=onion
  8 connect=127.0.0.1:18344
```

### bitcoind, bitcoin-cli
```
➜  doc git:(rpc_getorphantxs) ✗ currentbitcoind
bitcoind -datadir=/tmp/node1 -conf=/tmp/node1/bitcoin.conf -port=18000
bitcoind -datadir=/tmp/node2 -conf=/tmp/node2/bitcoin.conf -port=19000

bitcoincli -conf=/tmp/node1/bitcoin.conf getblockchaininfo
bitcoincli -conf=/tmp/node2/bitcoin.conf getblockchaininfo
```
