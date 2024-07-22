- After a new block arrives, the fee estimator listens for notifications of all transactions removed from mempool because of the new block, and updates their tracking stats.
- `CBlockPolicyEstimator::TransactionRemovedFromMempool`: https://github.com/bitcoin/bitcoin/blob/master/src/policy/fees.cpp#L582

- Assuming A->B->C->D are topologically sorted from parent to last descendant. In this case B, C, D are already not considered for fee estimation, After this PR A will also be ignored.
- FeeEstimator goal: https://github.com/bitcoin/bitcoin/blob/master/src/policy/fees.h#L144-L146
