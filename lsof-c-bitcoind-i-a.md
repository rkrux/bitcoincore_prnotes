```
➜  ~ bitcoindnetwork | grep "(LISTEN)"
bitcoind 53001 aither    9u  IPv6 0x6c2efd5ac3510257      0t0  TCP localhost:8332 (LISTEN)
bitcoind 53001 aither   10u  IPv4 0x548cefd88adcd258      0t0  TCP localhost:8332 (LISTEN)
bitcoind 53001 aither   20u  IPv4 0xfc3f1be687a78297      0t0  TCP localhost:8334 (LISTEN)
bitcoind 53001 aither   22u  IPv6 0x8f53e95961e86f1a      0t0  TCP *:8333 (LISTEN)
bitcoind 53001 aither   23u  IPv4 0xbbbed19ecbf9d186      0t0  TCP *:8333 (LISTEN)
bitcoind 55047 aither   10u  IPv4 0xd75c7588766b844b      0t0  TCP localhost:18343 (LISTEN)
bitcoind 55047 aither   20u  IPv4 0x48838b972d5e456a      0t0  TCP localhost:18344 (LISTEN)
bitcoind 55047 aither   22u  IPv4 0x7d2e63660b1fecce      0t0  TCP localhost:18345 (LISTEN)
```

`53001` belongs to the bitcoin core in mainnet. By default, core uses 8332/8333/8334 port ranges.
`55047` belongs to the bitcoin core in testnet with custom bind ports passed.
