emcc -O0 -s STANDALONE_WASM -s EXPORTED_FUNCTIONS="['_check']" -Wl,--no-entry "check.cpp" -o "../docker/app/check.js"
