package main

import "fmt"

var age int

func main() {
	fmt.Print("enter a age: ")
	fmt.Scan(&age)

	switch {
	case age == 32:
		fmt.Println("You are 32!")
	case age < 16:
		fmt.Println("You are too young to drive.")
	case age < 18:
		fmt.Println("You are too young to get a tattoo")
	case age < 21:
		fmt.Println("You are too young to drink!")
	case age > 60:
		fmt.Println("You are old!")

	default:
		fmt.Printf("You are %d years old!", age)
	}

}
