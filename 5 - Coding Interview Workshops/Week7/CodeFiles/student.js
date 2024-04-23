class Student {
    constructor (name, age, grade) {
        this.name = name;
        this.age = age;
        this.grade = grade;
    }

    sayMyName () {
        console.log(`Hi, my name is ${this.name}`);
    }
}

let zahra = new Student("Zahra", 23, 12);
console.log(zahra.name);

