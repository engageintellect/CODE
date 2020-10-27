package main

import (
    "fmt"
)

var x int
var y int


func main(){
    fmt.Println(add(x,y))
}


func add(x, y int) int {
    fmt.Print("enter a number: ")
    fmt.Scan(&x)
    fmt.Print("enter another number: ")
    fmt.Scan(&y)
    return x + y
}
