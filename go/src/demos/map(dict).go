package main

import (
    "fmt"
)

func main() {
    vertices := make(map[string]int)

    vertices["circle"] = 0
    vertices["triangle"] = 2
    vertices["square"] = 3
    vertices["dodecagon"] = 12

    delete(vertices, "circle")

    fmt.Println(vertices["square"])

    fmt.Println("\n")
    fmt.Println(vertices)
    


}
