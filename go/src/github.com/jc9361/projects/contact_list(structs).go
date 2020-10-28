package main

import (
	"fmt"
)

type contact struct {
	name      string
	phone     string
	email     string
	fave_food []string
}

func (x contact) hello() string {
	fmt.Println("CONTACT:", x.name)
	return x.name
}

func main() {
	p := contact{
		name:      "josh",
		phone:     "750-6530",
		email:     "jc9361@gmail.com",
		fave_food: []string{"pizza"},
	}

	r := contact{
		name:  "jeff",
		phone: "867-5309",
		email: "jeff@gmail.com",
	}

	p.hello()
	fmt.Print(p, "\n\n")

	r.hello()
	fmt.Print(r, "\n\n")

}
