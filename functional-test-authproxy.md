### Stack trace
```
Traceback (most recent call last):
  File "/Users/rkrux/projects/bitcoin/test/functional/test_framework/test_framework.py", line 132, in main
    self.run_test()
    ~~~~~~~~~~~~~^^
  File "/Users/rkrux/projects/bitcoin/build/test/functional/wallet_migration.py", line 1020, in run_test
    self.test_basic()
    ~~~~~~~~~~~~~~~^^
  File "/Users/rkrux/projects/bitcoin/build/test/functional/wallet_migration.py", line 119, in test_basic
    self.migrate_wallet(basic0)
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^
  File "/Users/rkrux/projects/bitcoin/build/test/functional/wallet_migration.py", line 73, in migrate_wallet
    return wallet_rpc.migratewallet(*args, **kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/Users/rkrux/projects/bitcoin/test/functional/test_framework/coverage.py", line 50, in __call__
    return_val = self.auth_service_proxy_instance.__call__(*args, **kwargs)
  File "/Users/rkrux/projects/bitcoin/test/functional/test_framework/authproxy.py", line 127, in __call__
    response, status = self._request('POST', self.__url.path, postdata.encode('utf-8'))
                       ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/rkrux/projects/bitcoin/test/functional/test_framework/authproxy.py", line 106, in _request
    return self._get_response()
           ~~~~~~~~~~~~~~~~~~^^
  File "/Users/rkrux/projects/bitcoin/test/functional/test_framework/authproxy.py", line 195, in _get_response
    raise JSONRPCException({
        'code': -342, 'message': f'Cannot decode response in utf8 format, content: {data}, exception: {e}'})
```

### Function call stack
```
wallet_rpc.migratewallet -> self.auth_service_proxy_instance.__call__ -> self._request -> self._get_response
```

### Functional test initialisation and start
```
SubClassTest(__file__).main()

1. __main__
  1. BitcoinTestFramework.__init__()
  2. SubClassTest.set_test_params() [Unimplemented in SubClassTest]
2. BitcoinTestFramework.main()
  1. BitcoinTestFramework.setup()
    1. BitcoinTestFramework.setup_chain()
      1. BitcoinTestFramework._initialize_chain()
    2. BitcoinTestFramework.setup_network()
      1. BitcoinTestFramework.setup_nodes()
        1. BitcoinTestFramework.add_nodes()
          1. loop(numNodes) -> new TestNode()
            1. TestNode.__init__()
        2. BitcoinTestFramework.start_nodes()
          1. loop(nodes) -> TestNode.wait_for_rpc_connection()
            1. get_rpc_proxy(rpcc_url)
              1. proxy = AuthServiceProxy(url)
                1. _request() [makes an HTTP request to the rpc]
                  1. _get_response()
              2. AuthServiceProxyWrapper(proxy, url)
  2. SubClassTest.run_test() [Unimplemented in SubClassTest]
```
