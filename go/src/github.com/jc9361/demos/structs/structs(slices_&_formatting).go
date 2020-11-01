package main

import "fmt"

type Customer struct {
	name  string
	phone string
	wants []string
	date  string
}

func (x Customer) say_hello() {
	fmt.Println("Hello", x.name)
}

func (x Customer) usr_greet() {
	fmt.Printf("\nHello %s, we will call you at %s to talk about %s.", x.name, x.phone, x.wants)
}

func main() {

	a := Customer{
		name:  "josh",
		phone: "949-750-6530",
		wants: []string{"food", "pizza", "other stuff"},
		date:  "12/12/12",
	}
	fmt.Println(a)

	var newlist = []string{}
	newlist = append(newlist, a.name, a.date, a.wants[0])
	fmt.Println(newlist)

	a.usr_greet()
}
