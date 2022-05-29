#!/usr/bin/env node


class Car {
    constructor(brand, model, year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
    }
}


myCar = new Car("Tesla", 3, 1966);
firstCar = new Car("Ford", "Focus", 2005);


console.log(myCar);
console.log(firstCar);

