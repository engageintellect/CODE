package main

import (
	"fmt"
	"os/exec"
	"time"
)

func main() {
	i := 0

	for i < 100000 {
		fmt.Print(i)
		time.Sleep(2 * time.Millisecond)
		i += 50
	}

	cmd()
	main()

}

func cmd() {
	fmt.Println("\n")
	cmd := exec.Command("figlet", " ", "R3DUX")
	stdout, err := cmd.Output()

	if err != nil {
		fmt.Println(err.Error())
		return
	}

	fmt.Print(string(stdout))

}
