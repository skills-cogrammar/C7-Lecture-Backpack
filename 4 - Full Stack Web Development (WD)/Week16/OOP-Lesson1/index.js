//Blueprint (Animal)
/**
 * name
 * Sound
 * Movement
 */
// class Animal {
//     constructor(name, sound, movement) {
//         //Constructor properties
//         this.name = name
//         this.sound = sound
//         this.movement = movement
//     }

//     //getters and setters
//     getName(){
//         return this.name
//     }

//     setName(name){
//         this.name = name
//     }

//     greet(){
//         return "Hello"
//     }
// }

// export default Animal


let person = {
    name : "Dan",
    role : "Programming lecturer"
}

let skills = {
    javacript : true,
    python: false
}

//Spread operator
let combined = {...person, ...skills}

//Iterate over properties inside a javascript object
// for (let property in person) {
//     console.log(person[property])
// }

const myJSON = JSON.stringify(person)

const normal = JSON.parse(myJSON)
console.log(normal)
