package main

import (
	"fmt"
)

// rect stuct
type rect struct {
	width  int
	height int
}

// struct functions
func (x rect) get_area() int {
	return x.width * x.height
}

func (x rect) get_perimeter() int {
	return x.width*2 + x.height*2
}

// rect 1 & 2 init
func rect1() {
	x := rect{
		width:  20,
		height: 50,
	}
	fmt.Println(x.get_area())
	fmt.Println(x.get_perimeter())

	y := rect{
		width:  300,
		height: 20,
	}
	fmt.Println(y.get_area())
	fmt.Println(y.get_perimeter())
}

// adding another rect
func rect2() int {
	x := rect{
		width:  123,
		height: 111,
	}

	return x.get_area()
	return x.get_perimeter()
}

func main() {
	rect1()
	fmt.Println(rect2())
}
