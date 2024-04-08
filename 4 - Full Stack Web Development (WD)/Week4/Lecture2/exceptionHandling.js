class Animal {
    constructor(name, noLegs, colour, environment){
        this.name = name;
        this.noLegs = noLegs;
        this.colour = colour;
        this.environment = environment;
    }
}

let zebra = new Animal("Zebra", 4, "Black and White", "Safari");
let snake = new Animal("Snake", 0, "Any", "Any");
let dolphin = new Animal("Dolphin", 0, "Grey", "Ocean");

let animals = [zebra, snake, dolphin];

let a = 10;
let b = 11;
let c = 12;

let list = [a, b, c];
list[0] = 3;
console.log(list[0]);
console.log(a);

animals[0].name = "African Zebra";
console.log(animals[0].name);
console.log(zebra.name);

function searchAnimal(name){
    let found = false;

    for (let animal in animals) {
        if (animal.name == name) {
            return animal;
        }
    }

    if (!found) {
        throw new Error(`Could not find animal ${name}`)
    }
}

try {
    searchAnimal("Cricket");
} catch (error) {
    if (error instanceof Error) {
        console.log("Error: ", error.message);
    }
}