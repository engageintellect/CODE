package main

import (
	"fmt"
)

type hours_to_moon struct {
	speed,
	distance int
}

func (m hours_to_moon) slingshot() int {
	return m.distance / m.speed

}

func main() {
	fmt.Println("HOURS TO THE MOON")
	fmt.Print("How fast are you going?: ")
	var x int
	fmt.Scan(&x)

	m := hours_to_moon{speed: x, distance: 225623}
	result := fmt.Sprintf("Traveling at %d mph, it would take %d hours to get to the moon which is %d miles away", m.speed, m.slingshot(), m.distance)
	fmt.Println(result)

}
