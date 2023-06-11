package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/", HandleRoot)
	http.HandleFunc("/feed", HandleFeed)
	http.ListenAndServe(":1337", nil)
}

func HandleRoot(w http.ResponseWriter, req *http.Request) {
	fmt.Fprintf(w, "Howdy, I am the hamster.")
	fmt.Fprintf(w, "Please go to /feed\n")
}

func HandleFeed(w http.ResponseWriter, req *http.Request) {
	cookieSet := false
	cookieVal := ""
	for _, cookie := range req.Cookies() {
		if cookie.Name == "brownie" {
			cookieSet = true
			cookieVal = cookie.Value
		}
	}
	if req.UserAgent() != "hamster-agent" {
		fmt.Fprintf(w, "🕴️ only hamster-agent is allowed\n")
	} else if req.Method != "PUT" {
		fmt.Fprintf(w, "⛳ %s invalid\n", req.Method)
	} else if req.Referer() != "hackyhamster.org" {
		fmt.Fprintf(w, "🛑 request must come from hackyhamster.org\n")
	} else if !(cookieSet) {
		fmt.Fprintf(w, "🍪 brownie not found\n")
	} else if cookieSet && cookieVal != "baked" {
		fmt.Fprintf(w, "🍪 brownie must be baked\n")
	} else {
		fmt.Fprintf(w, "🚩 he2023{s1mpl3_h34d3r_t4mp3r1ng}\n")
	}
}
