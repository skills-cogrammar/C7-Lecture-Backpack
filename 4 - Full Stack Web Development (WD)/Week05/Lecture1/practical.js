document.body.setAttribute("class", "dark");

// // Retrieve the element with the ID "myDiv"
// var element = document.getElementById("myElement");
// console.log(element);

// // Retrieve all elements with the class "container"
// var containers = document.getElementsByClassName("container");
// console.log(containers);
// console.log(containers[1]);

// // Retrieve all list item elements
// var listItems = document.getElementsByTagName("li");
// console.log(listItems);
// console.log(listItems[1]);

// // Retrieve the first paragraph element within a container
// var paragraph = document.querySelector(".container p");
// console.log(paragraph);

// // Retrieve all paragraph elements within a container
// var paragraphs = document.querySelectorAll(".container p");
// console.log(paragraphs);
// console.log(paragraphs[2]);

// Create a new paragraph element
let paragraph = document.createElement("p");
let heading = document.createElement("h1");

// Add text content to the paragraph
paragraph.textContent = "This is a new paragraph.";
heading.textContent = "I love pie";

// Append the paragraph to the body element
// document.body.appendChild(paragraph);
// document.body.insertBefore(heading, paragraph);

// Change inner HTML content of an element
document.getElementById("myElement").innerHTML = "<strong>New content</strong>";

// Set text content of an element
document.getElementById("myElement").textContent = "Updated text content";

// Set attribute value of an element
document.getElementById("myElement").setAttribute("class", "dark");

// Get the element to remove
let elementToRemove = document.getElementById("myElement");

// Remove the element from the DOM
elementToRemove.remove();
