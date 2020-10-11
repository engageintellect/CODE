package main

import(
    "fmt"
    "time"
)


func main() {
    // DEFINE USER INPUT
    var num1 int
    var num2 int
    // USER INPUT
    fmt.Print("Pick a number: ")
    fmt.Scan(&num1)
    fmt.Print("Pick a number: ")
    fmt.Scan(&num2)
    // RUN FUNCTIONS (add, mult)
    fmt.Print("\n")
    add(num1,num2)
    mult(num1,num2)

}



func add(x int, y int){
    z := x + y
    fmt.Println(z)
}

func mult(x int, y int){
    z := x * y
    fmt.Println(z)
}



