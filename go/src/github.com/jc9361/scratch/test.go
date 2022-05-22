package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Print("CHOOSE A COMMAND... ")
	fmt.Println("[loop1] [loop2] [multiply]")
	fmt.Print(": ")
	var x string
	fmt.Scan(&x)

	if x == "q" {
		os.Exit(0)
	}

	if x == "loop1" {
		loop1()
	} else if x == "loop2" {
		loop2()
	} else if x == "multiply" {
		multiply()
	} else {
		fmt.Println("WRONG INPUT")
		main()
	}

	fmt.Println("\n")
	main()
}

func loop1() {
	i := 0

	for i < 100000 {
		fmt.Println(i)
		i += 1
	}

}

func loop2() {
	names := []string{"josh", "james", "jim"}

	names[1] = "jess"
	names = append(names, "frank")
	names = append(names, "chris")

	for i := 0; i < len(names); i++ {
		fmt.Println(names[i])
	}

	fmt.Print(names[2])
}

func multiply() {
	fmt.Print("ENTER A NUMBER: ")
	var x int
	fmt.Scan(&x)

	fmt.Print("ENTER A NUMBER: ")
	var y int
	fmt.Scan(&y)

	result := x * y

	fmt.Println(result)
}
