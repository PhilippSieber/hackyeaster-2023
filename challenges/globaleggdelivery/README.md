# solution
- recognize that the file contains UTF-BOMs 
- split at the BOMs, interpret the BOMs to get characters / strings
- concatenate characters/strings

- Cyber Chef recipe
  - [recipe](https://gchq.github.io/CyberChef/#recipe=To_Hex('None',0)Find_/_Replace(%7B'option':'Regex','string':'fffe(.%7B2%7D)(.%7B2%7D)'%7D,'$2$1',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'feff(.%7B4%7D)'%7D,'$1',true,false,true,false))
  - apply to message.txt file
  - output: `006800650032003000320033007b007500370192005f00620030006d00350073005f0038007215f1005f006e00300037005f003831630077006100790035005f00310067006e0030007215f10064007d`
  - convert output using https://dencode.com/en/string/hex
  - `he2023{u7ƒ_b0m5s_8rᗱ_n07_8ㅣway5_1gn0rᗱd}`

# build
see `src/generate.py`
