# solution

The PIN is 29660145# and can for testing purpose also be entered in the java script console as code = "29660145", then press #

## expected way to solve

* Isolate wasm file
* Analyse in developer console or ghidra (disassemble / decompile and figure out logic)
* for Ghidra, install the [Plugin](https://github.com/nneonneo/ghidra-wasm-plugin/)

With Ghidra you find the PIN check in decompiled form like this (Exports -> check).
PIN is easily deductible:

```
void export::check(int *param1)

{
  int iVar1;
  
  if (*param1 == 0x32) {
    if (param1[1] == *param1 + 7) {
      if (param1[2] == param1[1] + -3) {
        iVar1 = param1[2];
        if ((((param1[3] == iVar1) && (param1[4] == iVar1 + -6)) && (param1[5] == iVar1 + -5)) &&
           ((param1[6] == iVar1 + -2 && (param1[7] == iVar1 + -1)))) {
          unnamed_function_1(param1);
        }
        else {
          unnamed_function_2(param1);
        }
      }
      else {
        unnamed_function_2(param1);
      }
    }
    else {
      unnamed_function_2(param1);
    }
  }
  else {
    unnamed_function_2(param1);
  }
  return;
}
```

## alternate solutions

* brute force method in Web Dev console (with 8 numbers it will take a while)
* Do some guesswork on XORing strings


# setup and build

First you need to get the tooling

```
sudo apt-get install emscripten
```

Then you just need to compile the cpp code:

```
cd src && ./prepare.sh && cd ..
```

# links

* https://wasmbyexample.dev/examples/strings/strings.c.en-us.html
* https://emscripten.org/docs/porting/connecting_cpp_and_javascript/embind.html#embind