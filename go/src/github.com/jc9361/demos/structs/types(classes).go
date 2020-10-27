package main

import (
    "fmt"
)

type person struct {
    name string
    age int
    weight int
}


type cat struct {
    name string
    age int
    weight int

}
func main() {
    p1 := person{name: "Josh", age:32, weight:155}
    c1 := cat{name: "Kalani", age:15, weight:22}
    c2 := cat{name: "LB", age:11, weight:24}

    fmt.Println(p1)
    fmt.Println(c1)
    fmt.Println(c2)





}

