package main

import (
	"fmt"
)

type contact struct {
	name  string
	phone string
	email string
}

func main() {
	var usr_name string
	var usr_phone string
	var usr_email string
	fmt.Scanln(&usr_name, &usr_phone, &usr_email)

	j := contact{
		name:  usr_name,
		phone: usr_phone,
		email: usr_email,
	}

	fmt.Print(j.name, "\n\n")
	fmt.Print(j.phone, "\n\n")
	fmt.Print(j.email, "\n\n")

}
