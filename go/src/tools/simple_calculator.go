package main

import (
    "fmt"
    "os"
    "os/exec"
)


// MAIN

func main() {
    clear()
    fmt.Print("ENTER A NUMBER: ")
    var num1 int
    fmt.Scan(&num1)
    clear()

    fmt.Print("CHOOSE A METHOD (+, -, *, /, %): ")
    var method string
    fmt.Scan(&method)
    clear()

    fmt.Print("ENTER ANOTHER NUMBER: ")
    var num2 int
    fmt.Scan(&num2)
    clear()

    if method == "q" {
        fmt.Println("byeee")
        os.Exit(0)
    }


    // FILTER

    if method == "+" {
        fmt.Println("RESULT: ", add(num1, num2))
    }
    if method == "-" {
        fmt.Println("RESULT: ", subtract(num1, num2))
    }
    if method == "/" {
        fmt.Println("RESULT: ", divide(num1, num2))
    }
    if method == "*" {
        fmt.Println("RESULT: ", multiply(num1, num2))
    }
    if method == "%" {
        fmt.Println("RESULT: ", remainder(num1, num2))
    }

}



// PROGRAM FUNCTIONS

func add(x, y int) int {
    return x + y
}
func subtract(x, y int) int {
    return x - y
}
func divide(x, y int) int {
    return x / y
}
func multiply(x, y int) int {
    return x * y
}
func remainder(x, y int) int {
    return x % y
}


// CLEAR DISPLAY

func clear(){
    cmd := exec.Command("clear")
    clear, err := cmd.Output()
    if err != nil{
        fmt.Println(err.Error())
    }
    fmt.Println(string(clear))
}
