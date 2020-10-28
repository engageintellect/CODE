package main

import (
	"fmt"
	"os/exec"
)

func main() {
	scan()
}

func scan() {
	cmd := exec.Command("lspci", "-vnn", "-d", "14e4:")
	output, _ := cmd.Output()

	fmt.Println(string(output))
}
