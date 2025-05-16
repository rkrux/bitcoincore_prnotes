## Buggy earlier flow

### How the wallet transactions could be missed until user manually rescans
Initial state: Wallet and Node are synced to disk (e.g. a Flush just happened),
 the coinbase of the tip is a wallet tx.

1. Tip is disconnected due to a reorg (block invalidated notification). This 
will change the status of affected wallet txns to Inactive (which will be synced
 with the wallet db immediately) - but neither the node chainstate nor the 
wallet best block locator will be flushed.
2. The node has an unclean shutdown for an unrelated reason (e.g. power goes off).
3. The node restarts: The node will be back at the original tip, the wallet 
locator too (so no rescan is triggered), but the wallet tx state is Inactive 
(and abandoned for coinbase txns).
4. The node reorgs once more to the better chain (previous tip).

Since the wallet best block location was never written on the disk - without the
invalidated tip/block, upon restart it comes out to be the same as the node's
chainstate tip, and thus a rescan never happens. Due to which the previously
inactive/abandoned transactions remain in the same start even though the node
reorg'ed to the previous tip that was invalidated that makes these inactive
wallet transactions valid. This leads to missing transactions and incorrect
balances until the user figures out to manually rescan.

## Correct flow now
Now after #30221 changes, the wallet best block locator is persisted on disk
right after the block is invalidated. Now if the node has an unclean shutdown,
this will be noted by the wallet & thus automatically a rescan will happen when
the wallet is loaded. And the previously inactivated transactions are accounted
for now leading to correct balances.
