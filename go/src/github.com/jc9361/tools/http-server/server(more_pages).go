package main

import (
    "fmt"
    "net/http"
)


func index_handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "HELLO WORLD, IT IS NICE TO SERVE YOU :)")
}

func files_handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "HELLO WORLD :)" + "\n")
    fmt.Fprintf(w, "THIS IS THE FILES PAGE TO YOUR SERVER :)" + "\n")
}

func main() {
    http.HandleFunc("/", index_handler)
    http.HandleFunc("/files/", files_handler)
    http.ListenAndServe(":8000", nil)
}


