package main

import(
    "fmt"
)


func main(){
    names :=[]string{"dave", "chris", "james"}

    for _, i := range names{
        fmt.Println(i)
    }

}
