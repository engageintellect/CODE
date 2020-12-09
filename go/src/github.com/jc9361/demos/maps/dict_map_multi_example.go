package main

import "fmt"


func dict1() {
	dict := map [interface{}] interface{} {
		"josh": "hello",
		"jim": "hey",
	}
	fmt.Println(dict)
}
func dict2() {
	dict2 := map [interface{}] interface{} {
		1: "heythere",
		2: "sup",
	}
	fmt.Println(dict2)
}
func dict3() {
	contacts := make(map[int] string)
	contacts[1] = "this is the first thing"
	contacts[2] = "this is the second thing"

	fmt.Println(contacts)
}
func dict4() {
	stuff := make(map[string] string)
	stuff["First Name"] = "Josh"
	stuff["Last Name"] = "Chadwick"

	fmt.Println(stuff)
}
func dict5() {
	more_stuff := make(map[string] int)
	more_stuff["route"] = 66
	more_stuff["PCH"] = 1
	more_stuff["interstate"] = 5

	fmt.Println(more_stuff)
}


func main() {
	dict1()
	dict2()
	dict3()
	dict4()
	dict5()
}
