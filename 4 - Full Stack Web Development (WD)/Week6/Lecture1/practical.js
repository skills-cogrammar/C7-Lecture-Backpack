// let promise = new Promise(function (resolve, reject) {
//   //do something
// });

// returns a promise

// let countValue = new Promise(function (resolve, reject) {
//   resolve("Foo");
// });

//   // executes when promise is resolved successfully

// countValue
//   .then((result) => {
//     console.log(result);
//   })
//   .then(function successValue1() {
//     console.log("You can call multiple functions this way.");
//   });

// returns a promise
// let countValue = new Promise(function (resolve, reject) {
//   reject(10000);
// });

//  // executes when promise is resolved successfully
countValue
  .then(function successValue(result) {
    console.log(result);
  })
  .catch(function errorValue(result) {
    console.log(`Error: ${result}`);
  });

// a promise
let promise = new Promise(function (resolve, reject) {
  setTimeout(function () {
    reject(1000);
  }, 4000);
});

// // async function
async function asyncFunc() {
  // wait until the promise resolves
  try {
    let result = await promise;

    console.log(result);
    console.log("hello");
  } catch (err) {
    console.log(`Error: ${err}`);
  }
}

// // calling the async function
// asyncFunc();

// a promise
// let promise = new Promise(function (resolve, reject) {
//     setTimeout(function () {
//         // resolve('Promise resolved');
//         reject("Promise rejected");
//     }, 4000);
// });
// // async function
// async function asyncFunc() {
//     try {
//         // wait until the promise resolves
//         let result = await promise;

//         console.log(result);
//     }
//     catch(error) {
//         console.log(`Error: ${error}`);
//     }
// }

// // calling the async function
// asyncFunc(); // Promise resolved
