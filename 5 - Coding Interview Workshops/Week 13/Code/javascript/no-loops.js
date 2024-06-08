
// Use the remainder of the moves to determine the index of the 
// first child who will need to move to the left 
// Split the original list into two based on the first child who will need to move 
// to the left
function get_final_order(children, moves){
    let index = children.length - (moves % children.length); // Get the last item that needs to be moved to the beginning
    let first_porition = children.slice(index); // Get the chldren who need to move to the left
    
    // Unlike Python, this will be O(n) due to how javascript joins strings.
    return first_porition.concat(children.slice(0, index)) // Join the two lists.
}

console.log(get_final_order([1, 2, 3, 4, 5], 2));
