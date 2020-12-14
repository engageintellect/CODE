package main

import "fmt"

func main() {
	name := "josh"

	for _, chr := range name {
		fmt.Printf("%c\n", chr)
	}

}
