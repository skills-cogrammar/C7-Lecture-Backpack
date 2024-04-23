// Interfaces don't exist in JavaScript
// All methods can be overridden and all functions are polymorphic
class Vehicle {
    constructor (make, model, year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    letsDrive () {
        console.log("Chug chhuug");
    }
}

class Motorbike extends Vehicle {
    letsDrive () { console.log("Zooom zooom"); }
}

class Car extends Vehicle {
    letsDrive () { console.log("Vroom vrooooom"); }
}

class Truck extends Vehicle {
    letsDrive () { console.log("Brruuum brrruuuum"); }
}

let motorbike = new Motorbike("Yamaha", "Road Star", 2004);
let car = new Car("Volkswagen", "Polo", 2006);
let truck = new Truck("Ford", "F-150", 2021);

let vehicles = [motorbike, car, truck];

vehicles.forEach((vehicle) => vehicle.letsDrive());


