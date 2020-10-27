package main

import "fmt"

type people struct {
	name     string
	age      int
	eyes     string
	weight   float64
	fav_food []string
}

func (p people) year_born() int {
	return p.age - 2020
}

func (p people) weight_kilos() float64 {
	result := p.weight / 2.2046
	return result
}

func (p people) years_till_100() int {
	return 100 - p.age
}

func main() {
	p := people{
		name:     "josh",
		age:      32,
		eyes:     "brown",
		weight:   155,
		fav_food: []string{"pizza", "brownies", "cheese"},
	}

	fmt.Print(p, "\n\n")
	fmt.Println("Year born:", p.year_born())
	fmt.Println("Weight in kilos:", p.weight_kilos())
	fmt.Println("Years till 100:", p.years_till_100())
	fmt.Print("Favorite foods: ", p.fav_food)

}
