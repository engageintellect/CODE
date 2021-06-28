package main

import (
	"net/http"
)

func main() {
	http.Handle("/", http.FileServer(http.Dir("./static/"))) //replace "satic" with dir name
	http.ListenAndServe(":10000", nil)                       //3000 can be replaced with any other avaiable port number

}
