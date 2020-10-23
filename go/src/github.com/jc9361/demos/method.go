package main

import "fmt"

// define a type of thing..
type rect struct {
	width, height int
}

//another example
type triangle struct {
	x, y, z int
}

// make a function for that thing..
func (r rect) area() int {
	return r.width * r.height
}

//another example
func (t triangle) perimeter() int {
	return t.x + t.y + t.z

}

//main function
func main() {

	//define the things you want to run

	r := rect{width: 10, height: 5}
	t := triangle{x: 10, y: 10, z: 20}

	//call for some data...

	fmt.Println("area:", r.area())
	fmt.Println("perimeter of triangle:", t.perimeter())

}
