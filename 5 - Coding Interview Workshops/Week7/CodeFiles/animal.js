class Animal {
    constructor (name) {
        this.name = name;
    }
    
    sayHi () {
        console.log(`Hi, I am a ${this.name}`);
    }
}
class Mammal extends Animal {
    constructor (name, gestationPeriod){
        super(name)
        this.gestation = gestationPeriod
    }
}

let mammal = new Mammal("Zebra", 12);
mammal.sayHi();

