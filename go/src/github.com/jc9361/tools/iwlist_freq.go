package main

import (
	"fmt"
	"os/exec"
)

func main() {
	scan()
}

func scan() {
	cmd := exec.Command("iwlist", "freq")
	output, _ := cmd.Output()

	fmt.Println(string(output))
}
