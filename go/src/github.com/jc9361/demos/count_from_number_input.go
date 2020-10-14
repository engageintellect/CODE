package main

import (
    "fmt"
)


func main(){
    x:=0
    fmt.Println(counter(x))
}

func counter(x int) int{
    fmt.Scan(&x)
    for x:=x; x<100000; x+=1{
        fmt.Println(x)
    }
    return x


}

