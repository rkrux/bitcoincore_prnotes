## Directory where tests data is stored temporarily (cleared after system restart)
```
➜  T echo $TMPDIR
/var/folders/6v/mpspb4bx4zzf3xr2z96hgq9h0000gn/T/
```

## Unit and Functional Tests directory
```
➜  T ls -l | grep test
drwxr-xr-x   10 rkrux  staff   320B Nov 20 17:37 test_common bitcoin # Unit
drwxr-xr-x    6 rkrux   staff   192B Nov 20 17:37 test_runner_?_🏃_20241120_173709 # Functional
```

## Disk Usage during functional tests run
```
➜  T du -h test_runner_$'\342\202\277'_🏃_20241120_173709
  0B	test_runner_₿_🏃_20241120_173709/p2p_segwit_305/node0/stdout
  0B	test_runner_₿_🏃_20241120_173709/p2p_segwit_305/node0/stderr
 24K	test_runner_₿_🏃_20241120_173709/p2p_segwit_305/node0/regtest/blocks/index
 17M	test_runner_₿_🏃_20241120_173709/p2p_segwit_305/node0/regtest/blocks
 20K	test_runner_₿_🏃_20241120_173709/p2p_segwit_305/node0/regtest/chainstate
  0B	test_runner_₿_🏃_20241120_173709/p2p_segwit_305/node0/regtest/wallets
 19M	test_runner_₿_🏃_20241120_173709/p2p_segwit_305/node0/regtest
 19M	test_runner_₿_🏃_20241120_173709/p2p_segwit_305/node0
  0B	test_runner_₿_🏃_20241120_173709/p2p_segwit_305/node1/stdout
  0B	test_runner_₿_🏃_20241120_173709/p2p_segwit_305/node1/stderr
8.0K	test_runner_₿_🏃_20241120_173709/p2p_segwit_305/node1/regtest/blocks/index
 17M	test_runner_₿_🏃_20241120_173709/p2p_segwit_305/node1/regtest/blocks
 12K	test_runner_₿_🏃_20241120_173709/p2p_segwit_305/node1/regtest/chainstate
  0B	test_runner_₿_🏃_20241120_173709/p2p_segwit_305/node1/regtest/wallets
 18M	test_runner_₿_🏃_20241120_173709/p2p_segwit_305/node1/regtest
 18M	test_runner_₿_🏃_20241120_173709/p2p_segwit_305/node1
 37M	test_runner_₿_🏃_20241120_173709/p2p_segwit_305
  0B	test_runner_₿_🏃_20241120_173709/feature_maxuploadtarget_304/node0/stdout
  0B	test_runner_₿_🏃_20241120_173709/feature_maxuploadtarget_304/node0/stderr
 28K	test_runner_₿_🏃_20241120_173709/feature_maxuploadtarget_304/node0/regtest/blocks/index
3.6M	test_runner_₿_🏃_20241120_173709/feature_maxuploadtarget_304/node0/regtest/blocks
 24K	test_runner_₿_🏃_20241120_173709/feature_maxuploadtarget_304/node0/regtest/chainstate
  0B	test_runner_₿_🏃_20241120_173709/feature_maxuploadtarget_304/node0/regtest/wallets
5.7M	test_runner_₿_🏃_20241120_173709/feature_maxuploadtarget_304/node0/regtest
5.7M	test_runner_₿_🏃_20241120_173709/feature_maxuploadtarget_304/node0
6.1M	test_runner_₿_🏃_20241120_173709/feature_maxuploadtarget_304
  0B	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node0/stdout
  0B	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node0/stderr
 12K	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node0/regtest/blocks/index
 17M	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node0/regtest/blocks
 12K	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node0/regtest/chainstate
 21M	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node0/regtest
 21M	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node0
  0B	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node1/stdout
  0B	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node1/stderr
 36K	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node1/regtest/blocks/index
 17M	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node1/regtest/blocks
 28K	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node1/regtest/chainstate
 48K	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node1/regtest/indexes/coinstats/db
 48K	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node1/regtest/indexes/coinstats
 36K	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node1/regtest/indexes/blockfilter/basic/db
1.0M	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node1/regtest/indexes/blockfilter/basic
1.0M	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node1/regtest/indexes/blockfilter
1.1M	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node1/regtest/indexes
 18M	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node1/regtest
 18M	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node1
  0B	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node3/stdout
  0B	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node3/stderr
 36K	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node3/regtest/blocks/index
 17M	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node3/regtest/blocks
 28K	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node3/regtest/chainstate
 17M	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node3/regtest
 17M	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node3
  0B	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node2/stdout
  0B	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node2/stderr
 36K	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node2/regtest/blocks/index
 17M	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node2/regtest/blocks
 28K	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node2/regtest/chainstate
 24K	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node2/regtest/indexes/txindex
 48K	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node2/regtest/indexes/coinstats/db
 48K	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node2/regtest/indexes/coinstats
 36K	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node2/regtest/indexes/blockfilter/basic/db
1.0M	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node2/regtest/indexes/blockfilter/basic
1.0M	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node2/regtest/indexes/blockfilter
1.1M	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node2/regtest/indexes
 18M	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node2/regtest
 18M	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303/node2
 75M	test_runner_₿_🏃_20241120_173709/feature_assumeutxo_303
  0B	test_runner_₿_🏃_20241120_173709/feature_block_309/node0/stdout
  0B	test_runner_₿_🏃_20241120_173709/feature_block_309/node0/stderr
8.0K	test_runner_₿_🏃_20241120_173709/feature_block_309/node0/regtest/blocks/index
1.0G	test_runner_₿_🏃_20241120_173709/feature_block_309/node0/regtest/blocks
 12K	test_runner_₿_🏃_20241120_173709/feature_block_309/node0/regtest/chainstate
  0B	test_runner_₿_🏃_20241120_173709/feature_block_309/node0/regtest/wallets
1.0G	test_runner_₿_🏃_20241120_173709/feature_block_309/node0/regtest
1.0G	test_runner_₿_🏃_20241120_173709/feature_block_309/node0
1.0G	test_runner_₿_🏃_20241120_173709/feature_block_309
1.2G	test_runner_₿_🏃_20241120_173709
```

## Disk Usage while unit tests run
```
➜  T du -h test_common\ bitcoin
2.8M	test_common bitcoin/826d29660f18c64049c58b48f532b02d02a7f76c3f408dd8e861401b20696a96/regtest/blocks
6.8M	test_common bitcoin/826d29660f18c64049c58b48f532b02d02a7f76c3f408dd8e861401b20696a96/regtest
6.9M	test_common bitcoin/826d29660f18c64049c58b48f532b02d02a7f76c3f408dd8e861401b20696a96
2.8M	test_common bitcoin/8b2d459c4778885fe91cd545d24520a8f551ef729b3e1d56bb7c6872f24c3d5f/regtest/blocks
3.2M	test_common bitcoin/8b2d459c4778885fe91cd545d24520a8f551ef729b3e1d56bb7c6872f24c3d5f/regtest
3.2M	test_common bitcoin/8b2d459c4778885fe91cd545d24520a8f551ef729b3e1d56bb7c6872f24c3d5f
  0B	test_common bitcoin/1e39649f6232745d268d6d01219f30e2636ea0847334ad5bac7054c81d73bfe8/regtest/blocks
4.0K	test_common bitcoin/1e39649f6232745d268d6d01219f30e2636ea0847334ad5bac7054c81d73bfe8/regtest
4.0K	test_common bitcoin/1e39649f6232745d268d6d01219f30e2636ea0847334ad5bac7054c81d73bfe8
 52K	test_common bitcoin/0621057ff6626061bdaee44533ce79b3de24b7b327740bdc8a573526124c2fb0/regtest/blocks/index
5.7M	test_common bitcoin/0621057ff6626061bdaee44533ce79b3de24b7b327740bdc8a573526124c2fb0/regtest/blocks
 28K	test_common bitcoin/0621057ff6626061bdaee44533ce79b3de24b7b327740bdc8a573526124c2fb0/regtest/chainstate
 40K	test_common bitcoin/0621057ff6626061bdaee44533ce79b3de24b7b327740bdc8a573526124c2fb0/regtest/chainstate_snapshot
7.8M	test_common bitcoin/0621057ff6626061bdaee44533ce79b3de24b7b327740bdc8a573526124c2fb0/regtest
7.8M	test_common bitcoin/0621057ff6626061bdaee44533ce79b3de24b7b327740bdc8a573526124c2fb0
1.8M	test_common bitcoin/f3297d9ed12db5a859886be2857558f6b1af177d7c40c59a530c9eb58ee7e228/blocks
1.8M	test_common bitcoin/f3297d9ed12db5a859886be2857558f6b1af177d7c40c59a530c9eb58ee7e228
du: test_common bitcoin/447d4e3a944d30eabeb3f4a11dbfabb4d598648451d3bb45dee7de5dc6129c3a: No such file or directory
  0B	test_common bitcoin/098a1aee1213c54b5454a9284480645d35d1c61c55e562d3548ecdd8f4e781da/regtest/blocks
4.0K	test_common bitcoin/098a1aee1213c54b5454a9284480645d35d1c61c55e562d3548ecdd8f4e781da/regtest
4.0K	test_common bitcoin/098a1aee1213c54b5454a9284480645d35d1c61c55e562d3548ecdd8f4e781da
  0B	test_common bitcoin/9b037808d744bb5221e80f6a66ef44f5034db0a5e19d9c09875ce8ab6cc7113a/blocks
4.0K	test_common bitcoin/9b037808d744bb5221e80f6a66ef44f5034db0a5e19d9c09875ce8ab6cc7113a
2.8M	test_common bitcoin/ed808d9dc60b67a946dc1a4f35740f943fbdc704b82bc8e30b886330b02b4903/regtest/blocks
3.1M	test_common bitcoin/ed808d9dc60b67a946dc1a4f35740f943fbdc704b82bc8e30b886330b02b4903/regtest
3.1M	test_common bitcoin/ed808d9dc60b67a946dc1a4f35740f943fbdc704b82bc8e30b886330b02b4903
4.0K	test_common bitcoin/4627f6e2b30ac9f8c0445fdcef79c9a2c335543a51dd46e570d6e3c6588752b9/blocks
3.1M	test_common bitcoin/4627f6e2b30ac9f8c0445fdcef79c9a2c335543a51dd46e570d6e3c6588752b9
2.8M	test_common bitcoin/209d268200f525bce49d00c3e1d284db54da2da31198cb0800c6e0f6b0c5b5f1/regtest/blocks
3.5M	test_common bitcoin/209d268200f525bce49d00c3e1d284db54da2da31198cb0800c6e0f6b0c5b5f1/regtest
3.5M	test_common bitcoin/209d268200f525bce49d00c3e1d284db54da2da31198cb0800c6e0f6b0c5b5f1
2.8M	test_common bitcoin/78b9eaf29d3c89d6a939326a5c1ef0d4873a353975491f62945f9d15d6bedac0/regtest/blocks
3.5M	test_common bitcoin/78b9eaf29d3c89d6a939326a5c1ef0d4873a353975491f62945f9d15d6bedac0/regtest
3.5M	test_common bitcoin/78b9eaf29d3c89d6a939326a5c1ef0d4873a353975491f62945f9d15d6bedac0
 33M	test_common bitcoin
```
