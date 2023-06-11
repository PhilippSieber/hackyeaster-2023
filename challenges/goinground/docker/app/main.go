package main

import (
	"fmt"
	"html"
	"net/http"
)

var htmlPage string = `
<html>
  <head>
    <link rel="stylesheet" href="https://unpkg.com/@picocss/pico@latest/css/pico.min.css"/>
	<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
  </head>
  <body style="height: 100%%; background-color: #ffffff; background-image: repeating-radial-gradient(circle at 0 0, transparent 0, #ffffff 10px), repeating-linear-gradient(#e6e6e6, #e6e6e6);">
  <main class="container-fluid">
      <div style="width:320px; margin:auto; background-color: #ffffff; background-image: repeating-radial-gradient(circle at 100%% 0, transparent 0, #555555 10px), repeating-linear-gradient(#333333, #333333); padding: 30px 20px 2px 20px; text-align:center; border-radius:8px;">
	    <i class="fa fa-cogs" style="font-size: 160px; color: white;"></i>
		<br/><br/>
        <h2>%s</h2>
      </div>
    </main>
  </body>
</html>
`

func main() {
	http.HandleFunc("/", HandleRequest)
	http.HandleFunc("/encrypt", HandleEncrypt)
	// only for testing! http.HandleFunc("/decrypt", HandleDecrypt)
	http.ListenAndServe(":2000", nil)
}

func HandleRequest(w http.ResponseWriter, req *http.Request) {
	fmt.Fprintf(w, htmlPage, "<a href='/encrypt?s=sample'>click me!</a>")
}

func HandleEncrypt(w http.ResponseWriter, req *http.Request) {
	s, ok := req.URL.Query()["s"]
	if !ok || len(s[0]) < 1 {
		fmt.Fprintf(w, htmlPage, html.EscapeString("d'Oh!"))
		return
	}
	fmt.Fprintf(w, htmlPage, html.EscapeString(EncryptValue(s[0])))
}

func HandleDecrypt(w http.ResponseWriter, req *http.Request) {
	s, ok := req.URL.Query()["s"]
	if !ok || len(s[0]) < 1 {
		fmt.Fprintf(w, htmlPage, html.EscapeString("d'Oh!"))
		return
	}
	fmt.Fprintf(w, htmlPage, html.EscapeString(DecryptValue(s[0])))
}

func EncryptValue(s string) string {
	result := ""
	if len(s)%2 == 1 {
		s = s + " "
	}
	for i := 0; i < len(s)/2; i++ {
		result = result + string(Rot(s[i*2+1], 4))
		result = result + string(Rot(s[i*2], 8))
	}
	return result
}

func DecryptValue(s string) string {
	result := ""
	for i := 0; i < len(s)/2; i++ {
		result = result + string(Rot(s[i*2+1], 18))
		result = result + string(Rot(s[i*2], 22))
	}
	return result
}

func Rot(b byte, i byte) byte {
	if b >= 'a' && b <= 'z' {
		if b >= 'a'+(26-i) {
			return b + i - 26
		} else {
			return b + i
		}
	}
	return b
}
