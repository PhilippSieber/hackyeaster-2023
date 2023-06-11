# solution
- find that `jq` is used to grep content
- basic query can be e.g.`name as $n | .street`
- not that only one line is output
- analyze the json structure using `path` function
  - since only one line is output, use `nth` and `join` functions
  - `name as $n | nth(7;path(..)) | join(",")`  
    `"covert,flag"`
  - -> covert.flag
- read the flag
  - `name as $n | .covert.flag`

allowed characters: a-z, space, +, . 0-9, : [] ()
