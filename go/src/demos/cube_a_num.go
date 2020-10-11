package main

import (
    "fmt"
)



func main(){
    num:=0
    fmt.Println(cube(num))

}

func cube(num int) int {
    fmt.Print("Enter a number to cube: ")
    fmt.Scan(&num)
    return num*num*num
}
