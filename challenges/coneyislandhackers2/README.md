# solution
- find an expression, which outputs the passphrase when being eval'd
- use eval in the web dev tools of a browser, or call `node` in a shell
- step 1: find an expression which contains all letters necessary  
  ```
  > eval("a={}+{}[1]+!1;a")
  '[object Object]undefinedfalse'
  ```
- step 2: find a valid name for the variable (letters, `$`, `_`, and `/` are forbidden)
  - [modifier letters](https://codepoints.net/search?gc=Lm) are allowed - see [here](https://mathiasbynens.be/notes/javascript-identifiers)
  ```
  > eval("ʰ={}+{}[1]+!1;ʰ")
  '[object Object]undefinedfalse'
  ```
- step 3: pick letters from the string; the `ʸ` can be used as-is
  ```
  > eval("ʰ={}+{}[1]+!1;ʰ[5]+ʰ[1]+ʰ[16]+ʰ[4]+'ʸ'+ʰ[20]+ʰ[27]+ʰ[26]+ʰ[25]+ʰ[16]+ʰ[17]");
  'coneʸisland'
  ```
- enter the string in the web app  
  `ʰ={}+{}[1]+!1;ʰ[5]+ʰ[1]+ʰ[16]+ʰ[4]+'ʸ'+ʰ[20]+ʰ[27]+ʰ[26]+ʰ[25]+ʰ[16]+ʰ[17]`
