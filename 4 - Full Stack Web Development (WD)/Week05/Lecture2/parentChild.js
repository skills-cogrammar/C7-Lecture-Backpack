// Create To do list
let todo = ["Make up bed", "Wash dishes", "Feed rabbit"];
let todoElements = [];

// Make a list
const ul = document.createElement("ul");
document.body.appendChild(ul);

const li1 = document.createElement("li");
const li2 = document.createElement("li");

li1.textContent = todo[0];
li2.textContent = todo[1];

ul.appendChild(li1);
ul.appendChild(li2);
todoElements.push(li1);
todoElements.push(li2);

function hide(evt) {
  // evt.target refers to the clicked <li> element
  // This is different than evt.currentTarget, which would refer to the parent <ul> in this context
  evt.target.style.visibility = "hidden";
  let pos = todoElements.findIndex((element) => element == evt.target);
  todoElements.pop(pos);
  todo.pop(pos);

  console.log(todo);
}

// Attach the listener to the list
// It will fire when each <li> is clicked
ul.addEventListener("click", hide, false);
