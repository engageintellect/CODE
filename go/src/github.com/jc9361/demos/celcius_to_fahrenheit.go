package main

import "fmt"

func main() {
	var ftemp float64 = 0
	var ctemp float64 = 0

	fmt.Printf("enter a temp in celsius: ")
	fmt.Scanf("%f", &ctemp)
	ftemp = (ctemp * 1.8) + 32
	fmt.Printf("temp in f: %.2f", ftemp)

}
