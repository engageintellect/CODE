package main

import "fmt"

const name, age, weight, birthplace = "josh", 32, 155, "Honolulu, HI"

func main() {
	s := fmt.Sprintf("hello %s, you are %d, you weig %d, and were born in %s.", name, age, weight, birthplace)
	fmt.Println(s)
}
