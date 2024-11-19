## Bitcoin Core specific aliases and env vars for the `zshrc` file in Mac

```
# Global Path env var
export PATH=/usr/local/opt/ccache/libexec:$PATH
export PATH="/usr/local/opt/gnu-sed/libexec/gnubin:$PATH"
export PATH="/usr/local/opt/grep/libexec/gnubin:$PATH"

# Bitcoin directories vars
export BITCOIN_DATA_DIR="~/Library/ApplicationSupport/Bitcoin"
export BITCOIN_SRC_DIR="~/projects/bitcoin/src
export BITCOIN_BUILD_DIR="~/projects/bitcoin/build
export BITCOIN_BUILD_SRC_DIR="~/projects/bitcoin/build/src
export BITCOIN_BUILD_TEST_DIR="~/projects/bitcoin/build/test

# Conf files vars
export BITCOIN_CONF_REG=$BITCOIN_DATA_DIR/bitcoin-reg.conf
export BITCOIN_CONF_TEST=$BITCOIN_DATA_DIR/bitcoin-test.conf
export BITCOIN_CONF_MAIN=$BITCOIN_DATA_DIR/bitcoin-main.conf
export BITCOIN_CONF_SIG=$BITCOIN_DATA_DIR/bitcoin-sig.conf

# open/cd bitcoin dirs
alias cdbitcoindatadir="cd $BITCOIN_DATA_DIR"
alias openbitcoinconf="vi $BITCOIN_DATA_DIR/bitcoin.conf"
alias cdbitcoinsource="cd ~/projects/bitcoin/src"

# execute bitcoind and bitcoin-cli aliases
alias bitcoinclireg="$BITCOIN_BUILD_SRC_DIR/bitcoin-cli -conf=$BITCOIN_CONF_REG"
alias bitcoinclitest="$BITCOIN_BUILD_SRC_DIR/bitcoin-cli -conf=$BITCOIN_CONF_TEST"
alias bitcoinclimain="$BITCOIN_BUILD_SRC_DIR/bitcoin-cli -conf=$BITCOIN_CONF_MAIN"
alias bitcoindreg="$BITCOIN_BUILD_SRC_DIR/bitcoind -datadir=$BITCOIN_DATA_DIR -conf=$BITCOIN_CONF_REG"
alias bitcoindtest="$BITCOIN_BUILD_SRC_DIR/bitcoind -datadir=$BITCOIN_DATA_DIR -conf=$BITCOIN_CONF_TEST"
alias bitcoindmain="$BITCOIN_BUILD_SRC_DIR/bitcoind -datadir=$BITCOIN_DATA_DIR -conf=$BITCOIN_CONF_MAIN"
alias bitcoind="$BITCOIN_BUILD_SRC_DIR/bitcoind"
alias bitcoindprune="$BITCOIN_BUILD_SRC_DIR/bitcoind -prune=1024"

# Build and test
alias bitcoinmakeall="cmake --build build -j "$(($(nproc)+1))""
alias bitcoinrunfunctest="$BITCOIN_BUILD_TEST_DIR/functional/test_runner.py"
alias bitcoinconfigure="cmake -B build -DBUILD_GUI=ON -DWITH_BDB=OFF -LH"
alias bitcoinunittest="ctest --test-dir build -j "$(($(nproc)+1))""

alias bitcoinclean="git clean -fd"

# bitcoind details
alias currentbitcoind="ps aux | grep bitcoind"
alias bitcoindnetwork="lsof -c bitcoind -i -a"
alias bitcoindallfiles="lsof -c bitcoind"

alias bitcoindstorage="du -h $1" #bitcoindstorage $DATA_DIR_28
alias bitcoinoutputpfiles="find . -type f -name '*.o' -ls"

:checkoutpr() {
 # $1=27052; $2=2023-02-getpeerinfo
 git fetch origin pull/$1/head:$2
 git switch $2
}

```