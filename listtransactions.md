The `listtransactions` RPC would show a transaction as `bip125-replaceable: yes` if the transaction is in the mempool like below.

```
{
    "address": "tb1qma0mht3gfpluagjk07c3z0zsxgcdm58k3xtujj",
    "category": "send",
    "amount": -9.00000000,
    "label": "",
    "vout": 1,
    "fee": -0.00000147,
    "confirmations": 0,
    "trusted": true,
    "txid": "5d1df7d647a299a4f9ff58b200667d14ee8ac4bffc1d444c66d2a18842445d81",
    "wtxid": "c58089e74779e80a4779c0756dcb8bc9ee741c15154b79654115b3d4d0933d18",
    "walletconflicts": [
    ],
    "mempoolconflicts": [
    ],
    "time": 1726561190,
    "timereceived": 1726561190,
    "bip125-replaceable": "yes",
    "abandoned": false
  }
```

However, once the transaction is confirmed, the output shows as no for the said property and rightly so.
```
  {
    "address": "tb1qma0mht3gfpluagjk07c3z0zsxgcdm58k3xtujj",
    "category": "send",
    "amount": -9.00000000,
    "label": "",
    "vout": 1,
    "fee": -0.00000147,
    "confirmations": 19,
    "blockhash": "00000000b09ff20f2b9f06425c236be6eaf704385e867ba773bec31d7e70a7bd",
    "blockheight": 45446,
    "blockindex": 4,
    "blocktime": 1726563434,
    "txid": "5d1df7d647a299a4f9ff58b200667d14ee8ac4bffc1d444c66d2a18842445d81",
    "wtxid": "c58089e74779e80a4779c0756dcb8bc9ee741c15154b79654115b3d4d0933d18",
    "walletconflicts": [
    ],
    "mempoolconflicts": [
    ],
    "time": 1726561190,
    "timereceived": 1726561190,
    "bip125-replaceable": "no",
    "abandoned": false
  }
```

The `address` in this `send` transaction is the receiver though, which is confusing. Related issue: https://github.com/bitcoin/bitcoin/issues/28797
