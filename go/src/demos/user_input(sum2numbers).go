package main


import (
    "fmt"
)


func main() {

    fmt.Print("ENTER NUMBER: ")
    var x int
    fmt.Scan(&x)
    

    fmt.Print("ENTER ANOTHER NUMBER: ")
    var y int
    fmt.Scan(&y)

    sum :=  x + y


    fmt.Println(sum)



}
