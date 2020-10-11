package main

import (
    "fmt"
    "os/exec"
)



// MAIN FUNCTION
func main() {
    // INITIALIZE VARIABLES
    num := 0
    name := ""
    usr := ""
    x:=0
    y:=0

    // MAIN FUNCTIONS CALLS
    fmt.Println("MATH SHORTCUTS")
    fmt.Println(cube(num))
    fmt.Println(hello(name))
    usr_cmd(usr)
    fmt.Println(add(x,y))
}



// USR CMD
func usr_cmd(usr string) {

    fmt.Scan(&usr)
    cmd:=exec.Command(usr)
    stdout, err:=cmd.Output()
    if err != nil {
        fmt.Println(err.Error())
        return
    }
    fmt.Println(string(stdout))
}

// GREETER
func hello(name string) string {
    fmt.Print("What is your name?:")
    fmt.Scan(&name)
    return "hello" + name
}

// CUBE A NUM
func cube(num int) int {
    fmt.Print("Enter a number to cube:")
    fmt.Scan(&num)
    return num*num*num
}

func add(x, y int) int {
    fmt.Scan(&x, &y)
    return x + y

}




