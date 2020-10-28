package main

import "fmt"

func main() {
	fmt.Print("counting...\n\n")

	for i := 0; i < 10; i++ {
		defer fmt.Println(i) // notice how this prints in reversr order!
	}

	fmt.Print("done\n\n")
}
