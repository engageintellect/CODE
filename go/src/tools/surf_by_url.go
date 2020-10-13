package main


import (
    "fmt"
    "os/exec"
)



var x string = "" 



func main(){
    clear_screen()
    surf()
}


func get_url(x string) string {
    fmt.Print("enter a url: ")
    fmt.Scan(&x)
    url := x
    fmt.Println("your entered", url)
    return url
}

func surf(){
    cmd:=exec.Command("surf", string(get_url(x)))
    stdout, err := cmd.Output()
    if err != nil {
        fmt.Println(err.Error())
        return
    }
    fmt.Println(string(stdout))
}

func clear_screen(){
    cmd:=exec.Command("clear")
    stdout, err := cmd.Output()
    if err != nil {
        fmt.Println(err.Error())
        return
    }
    fmt.Println(string(stdout))
}







