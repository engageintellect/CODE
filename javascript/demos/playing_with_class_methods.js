class Car{
    constructor(brand, year, color){
        this.brand = brand;
        this.year = year;
        this.color = color;
    }

    describe_car(){
        console.log(`this car is a ${this.brand}, it was made in ${this.year}, and is the color ${this.color}`)
        return this;
    }

    save_car(){
        console.log(`this ${this.color} ${this.brand} from ${this.year} saved to db`)
        return this;
    }

}

let car_list = [

var carOne = new Car("honda", "1999", "red");
var carTwo = new Car("BMW", "2021", "white");
var carThree = new Car("Toyota", "2022", "grey");

]



for (let i = 0; i < car_list.length; i++) {
    console.log(car_list[i].describe_car().save_car());
}

