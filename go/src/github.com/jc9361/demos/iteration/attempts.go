package main

import (
	"fmt"
	"os"
	"os/exec"
)

func main() {
	clear()
	attempts()
}

func clear() {
	cmd := exec.Command("clear")
	output, _ := cmd.Output()

	fmt.Println(string(output))
}

func attempts() {
	tries := 0
	for tries < 10 {
		tries++
		fmt.Printf("hello josh, this is try # %d\n", tries)
		var name string
		fmt.Print("what is your name?: ")
		fmt.Scan(&name)
		if name == "q" {
			fmt.Println("Exiting Program...")
			os.Exit(0)
		} else if name == "josh" {
			fmt.Println(name)
		} else {
			fmt.Println("poop")
		}

	}
}
