package main

import "fmt"


func main() {
    fmt.Print("CHOOSE METHOD...")
    fmt.Print("add, subtract, multiply")
    fmt.Print("\n")

    var choose string
    fmt.Scan(&choose)

    if choose == "add" {
        add()
    } else if choose == "subtract" {
        subtract()
    }
    




    main()

}


func add() {
    fmt.Print("ENTER A NUMBER: ")
    var x int
    fmt.Scan(&x)
    
    fmt.Print("ENTER ANOTHER NUMBER: ")
    var y int
    fmt.Scan(&y)

    result := x + y

    fmt.Println(result)
    
}

func subtract() {
    fmt.Print("ENTER A NUMBER: ")
    var x int
    fmt.Scan(&x)
    
    fmt.Print("ENTER ANOTHER NUMBER: ")
    var y int
    fmt.Scan(&y)

    result := x - y

    fmt.Println(result)
    
}

func multiply() {
    fmt.Print("ENTER A NUMBER: ")
    var x int
    fmt.Scan(&x)
    
    fmt.Print("ENTER ANOTHER NUMBER: ")
    var y int
    fmt.Scan(&y)

    result := x * y

    fmt.Println(result)
    
}

