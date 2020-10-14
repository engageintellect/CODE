package main

import (
    . "fmt"
    "time"
)


func main() {
    fast()

}




func fast() {
    for x := 0; x<100000; x+=1 {
        Print(x)
    }
    slow()
}


func slow() {
    num := 0

    for num=num; num < 100; num+=2 {
        time.Sleep(50 * time.Millisecond)
        Println(num)
    }
    fast()
}



