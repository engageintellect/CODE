package main

import "fmt"

type People struct {
	name string
	age  int
}

func (x People) say_hello() {
	// F STRING
	fmt.Printf("hello %s, you are %d years old.", x.name, x.age)
	// F STRING
}

func main() {
	x := People{
		name: "josh",
		age:  32,
	}

	fmt.Println(x)
	x.say_hello()
}
