package main

import (
    "fmt"
)


func main(){
    name:=""
    last:=""
    hello(name, last)
}

func hello(name, last string) {
    fmt.Print("what is your name?: ")
    fmt.Scan(&name)

    if name != "josh"{
        fmt.Println("hi")
    } else {
        fmt.Println("hello", name)
    }
    fmt.Print("what is your last name?: ")
    fmt.Scan(&last)
    fmt.Println("your full name is", name, last)
}


