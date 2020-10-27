package main

import "fmt"

func main() {

	list1 := []int{1, 2, 3, 4, 5}
	list2 := []int{6, 7, 8, 9, 10}
	list3 := []int{11, 12, 13, 14, 15}

	x := []int{}
	x = append(list1, list2...) // Can't concatenate more than 2 slice at once
	x = append(x, list3...)     // concatenate x with c

	fmt.Println(x)

}
