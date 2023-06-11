# solution

## IDOR

1. Create a new user, eg. with username "test"
2. Create a new password entry (Add Password)
3. Call "show password" and catch the url, eg. [http://ch.hackyeaster.com:2312/get/13](http://ch.hackyeaster.com:2312/get/13)
4. Modify URL to [http://ch.hackyeaster.com:2312/get/7](http://ch.hackyeaster.com:2312/get/7) and get the flag. The id = 7 can be found by:
  * guessing
  * doing SQLI (see below)

## SQLI

You can see the vault in the database using SQLI in the search form:

```
' union select id, id, title, url, username, password from safe -- 
```

You only see the encrypted password (each with a different IV), so only bruteforcing is feasible. But you could get knowledge about the id of the vault entry containing the flag.