package main

import "fmt"

func main() {
	// MAKE A MAP
	contacts := make(map[string]string)

	contacts["name"] = "Josh"
	contacts["age"] = "32"
	contacts["birthday"] = "09/07/1988"
	contacts["birthplace"] = "Honolulu, HI"

	// ITERATE OVER MAP
	for x, y := range contacts {
		fmt.Println(x, y)
	}

	// PRINT MAP ELEMENTS USING KEY
	fmt.Println(contacts["name"])
	fmt.Println(contacts["age"])

}
