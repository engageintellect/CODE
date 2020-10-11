package main

import "os/exec"
import . "fmt"


func main() {
    scan()

}

func scan() {
    cmd := exec.Command("sudo", "arp-scan", "--localnet")
    stdout, err := cmd.Output()

    if err != nil {
        Println(err.Error())
        return
    }

    Print(string(stdout))
}

