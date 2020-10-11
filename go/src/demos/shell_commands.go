package main

import "os/exec"
import . "fmt"


func main() {
    ls()
    pwd()

}

func ls() {
    cmd := exec.Command("ls")
    stdout, err := cmd.Output()

    if err != nil {
        Println(err.Error())
        return
    }

    Print(string(stdout))
    Print("\n")
}


func pwd() {
    cmd := exec.Command("pwd")
    stdout, err := cmd.Output()

    if err != nil {
        Println(err.Error())
        return
    }

    Print(string(stdout))
    Print("\n")
}
