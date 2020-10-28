package main

import "os/exec"
import . "fmt"

func main() {
	scan()

}

func scan() {
	cmd := exec.Command("ping", "-c 3", "google.com")
	stdout, err := cmd.Output()

	if err != nil {
		Println(err.Error())
		return
	}

	Print(string(stdout))
}
