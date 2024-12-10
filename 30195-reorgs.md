https://learnmeabitcoin.com/technical/blockchain/chain-reorganisation/
> A chain reorganisation (or "reorg") takes place when your node receives blocks that are part of a new longest chain. Your node will deactivate blocks in its old longest chain in favour of the blocks that build the new longest chain. This process allows individual nodes across the network to agree on the same version of the blockchain, because the globally accepted view of the blockchain will always be the one with the longest* chain of blocks.

https://github.com/bitcoin/bitcoin/pull/30195#discussion_r1643329094
> There is a reorg happening, nodes 0 and 1 mine 6 blocks on top of the common ancestor, while 2 and 3 mine 7 blocks. When the network is rejoined, the 7 block branch reorgs the 6 block branch. However, nodes1_last_blockhash is the tip of the 6 block branch which is not in the main chain.

To simulate reorgs in the functional tests:

- Split the network into two sub networks
- Mine different length blocks on each side
- Join the network into one, and then the longer chain will reorg the shorter one

```
        # Split network into two
        self.split_network()

        # generate on both sides
        nodes1_last_blockhash = self.generate(self.nodes[1], 6, sync_fun=lambda: self.sync_all(self.nodes[:2]))[-1]
        self.generate(self.nodes[2], 7, sync_fun=lambda: self.sync_all(self.nodes[2:]))[0]

        self.join_network()
```

