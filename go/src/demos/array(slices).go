package main

import (
    "fmt"
)

func main() {
    a := []int{1,2,3,4,5}
    a[2] = 9

    a = append(a, 13)


    


    fmt.Println(a)
}
