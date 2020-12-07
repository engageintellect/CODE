package main

import "fmt"

func main() {
	dict := map[interface{}]interface{}{
		"josh": "hello",
		"jim":  "hey",
	}

	fmt.Println(dict)

}
