const periodicTable = document.getElementById("periodic-table");

// The colors of the different groups in our periodic table
const colours = {
    "alkali metal": "#ffc6ff",
    "alkaline earth metal": "#bdb2ff",
    "transition metal": "#a0c4ff",
    "lanthanoid": "#9bf6ff",
    "actinoid": "#caffbf",
    "metalloid": "#fdffb6",
    "nonmetal": "#ffd6a5",
    "halogen": "#ffadad",
    "noble gas": "#f07167",
    "metal": "#e9ff70",
    "post-transition metal": "#e5383b"

}

/**
 * Create the cells and inserts the elements into our periodic table
 */
async function generateCells(){
    let dimensions = 9 * 18;    

    for (let i = 0; i < dimensions; i++) {
        const cell = document.createElement("div");
        cell.classList.add("cell");
        let htmlComponents = `<h3 class="atomic-number"></h3> <h2 class="element"></h2>`       
        cell.innerHTML = htmlComponents;        
        periodicTable.appendChild(cell);
    }

    await addElementsToTable();
}

/**
 * Gets the elements from the elements.json file
 * @returns A list of elements from the elements.json file
 */
function getElements(){
    return new Promise((resolve, reject) => {
        fetch('elements.json')
        .then(response => response.json())
        .then(data => resolve(data))
        .catch(error => reject(error))
    });        
}

/**
 * Adds the elements to the table
 */
async function addElementsToTable(){
    let elements = await getElements();
    let cells = document.querySelectorAll(".cell");

    for (let element of elements) {
        const listIndex = getListIndexOfElement(element.period, element.group);
        cells[listIndex].querySelector(".atomic-number").textContent = element.atomicNumber;
        cells[listIndex].querySelector(".element").textContent = element.symbol;
        cells[listIndex].setAttribute("data-listIndex", listIndex);
        cells[listIndex].style.backgroundColor = colours[element.groupBlock];
                
        // await new Promise(resolve => setTimeout(resolve, 1000));
    }    
}

/**
 * Gets the position in a 1D list based on the 2D list index
 * @param {number} period The period of the element
 * @param {number} group The group of the element
 * @returns List index
 */
function getListIndexOfElement(period, group){
    console.log(period, group)
    result = (--period * 18) + --group;
    return result
}

generateCells();