package main

import (
    "fmt"
)

func main() {
    fmt.Print("ENTER FIRST NAME: ")
    first := ""
    fmt.Scan(&first)

    fmt.Print("ENTER LAST NAME: ")
    last := ""
    fmt.Scan(&last)


    fmt.Print("\n")


    fmt.Print("YOUR FULL NAME IS: ")

    fmt.Print(first + " " + last)

}
