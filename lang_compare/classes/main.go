package main

import "fmt"

type rect struct {
	height int
	width  int
}

func (x rect) area() int {
	return x.height * x.width
}

func (x rect) perimeter() int {
	return x.height*2 + x.width*2
}

func main() {
	a := rect{
		height: 10,
		width:  10,
	}

	fmt.Println(a.area())
	fmt.Println(a.perimeter())
}
