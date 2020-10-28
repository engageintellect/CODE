package main


import (
	"fmt"
)



type Triangle struct {
	x float64
	y float64
	z float64
}



func (x Triangle) tri_perim() float64 {
	return x.x + x.y + x.z
}



func (x Triangle) base() {
	if x.x > x.y {
		if x.x > x.z {
			fmt.Print("x is biggest")
		}
	}
	if x.y > x.z {
		if x.y > x.x {
			fmt.Print("y is biggest")
		}
	} else {
		fmt.Print("z is biggest")
	}
}



func main() {
	t1 := Triangle{
		x: 600,
		y: 810,
		z: 900,
	}

	fmt.Print("TRIANGLE T1\n")
	fmt.Println("SIDE X", t1.x)
	fmt.Println("SIDE Y", t1.y)
	fmt.Print("SIDE Z", t1.z, "\n")
	fmt.Println("TRIGANLGE PERIMETER:", t1.tri_perim())
	t1.base()
}
