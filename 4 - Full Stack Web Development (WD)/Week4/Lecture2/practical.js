// throw new Error("We can thow errors on our own too yeeeeh.");

// try {
//     // Code that may throw an exception
//     console.log(`Name: ${personName}`);
// } catch (error) {
//     // Handle the error
//     console.log("Error caught:", error.message);
// } finally {
//     console.log("Byeeeee!");
// }

// function foo() {
//     throw new Error("An error occurred in foo.");
// }

// function bar() {
//     foo();
// }

// try {
//     bar();
// } catch (error) {
//     console.log("Error caught:", error.message);
// }

// try {
    // let m = 6;
    // console.log(m.map(m => m.speed));
    // console.log(zahir)
// } catch (error) {
  
//     if (error instanceof TypeError) {
//         console.log("Type error:", error.message);
//     } else if (error instanceof ReferenceError) {
//         console.log("Reference error:", error.message);
//     } else {
//         console.log("Other error:", error.message);
//     }
// }

// class ZahirError extends Error {
//     constructor(){
//         super("Your name is not zahir.")
//         this.name = "YouAreNotZahirError";
//     }

// }

// let firstName = "John";
// try {
//     if(firstName != "Zahir"){
//         throw new ZahirError()
//     }
// } catch (error) {
//     console.log(`${error.name}: ${error.message}`)
// }

// class zahir extends Error {
//     constructor(message) {
//         super(message);
//         this.name = "MyCustomError";
//     }
// }

// try {
//     throw new zahir("An error occurred.");
// } catch (error) {
//     console.log("Error caught:", error.name, "-", error.message);
// }
