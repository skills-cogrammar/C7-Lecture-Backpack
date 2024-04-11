let cells = document.querySelectorAll(".cell");
let message = document.getElementById("message");
message.textContent = "Let's Begin";

let currentPlayer = "X";
let winner = null;
let moves = 0;

cells.forEach((cell) => {
  cell.addEventListener("click", handleClick);
});

function handleClick(event) {
  let cell = event.target;
  let index = cell.getAttribute("data-index");

  if (cell.textContent === "" && !winner) {
    cell.textContent = currentPlayer;
    moves++;
  }

  if (checkWin()) {
    winner = currentPlayer;
  } else if (moves >= 9) {
    winner = "Draw";
  } else {
    currentPlayer = currentPlayer === "X" ? "O" : "X";
    // condition ? true_val : false_val;
  }

  if (winner) {
    // if winner != ""
    displayWinner();
  }
}

function checkWin() {
  let winPatterns = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];

  for (let pattern of winPatterns) {
    let [a, b, c] = pattern;

    if (
      cells[a].textContent !== "" &&
      cells[a].textContent === cells[b].textContent &&
      cells[a].textContent === cells[c].textContent
    ) {
      // To check for player that won
      return true;
    }
  }

  return false;
}

function displayWinner() {
  if (winner === "Draw") {
    message.textContent = "It's a draw!";
  } else {
    message.textContent = `Player ${winner} wins!`;
  }
}
