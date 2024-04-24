const periodicTable = document.getElementById("periodic-table");

for (let i = 1; i <= 9; i++) {
    for (let j = 1; j <= 18; j++) {
        const cell = document.createElement("div");        
        cell.textContent = `${i}, ${j}`;        
        cell.classList.add("cell"); 
        periodicTable.appendChild(cell);
    }
}

const cells = document.querySelectorAll(".cell");

let x = 6;
let y = 8;

let position = (--x * 18) + --y;

cells[position].style.backgroundColor = "red";

function PeriodicElement(symbol, name, period, group){
    this.symbol = symbol;
    this.name = name;
    this.period = period;
    this.group = group;
}

const elements = [
    new PeriodicElement("H", "Hydrogen", 1, 1),
    new PeriodicElement("He", "Helium", 1, 18),
    new PeriodicElement("Li", "Lithium", 2, 1),
    new PeriodicElement("Be", "Beryllium", 2, 2),
    new PeriodicElement("B", "Boron", 2, 13),
    new PeriodicElement("Os", "Osmium", 6, 8),
]


function getListIndexOfElement(period, group){
    return (--period * 18) + --group;
}

for (let element of elements) {
    const listIndex = getListIndexOfElement(element.period, element.group);
    cells[listIndex].textContent = element.symbol;
}