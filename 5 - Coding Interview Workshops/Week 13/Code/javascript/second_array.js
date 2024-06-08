// Create a second list where each child will be moved to their final position directly
function get_final_order(children, moves){
    const final_order = new Array(children.length); // Create the output array

    for (let seat = 0; seat < children.length; seat++) { // Go through each child
        // Get the childs correct seat, % will make sure that the 
        // Seat is in the correct range
        let next_seat = (seat + moves) % children.length; 

        // Add the child to their correct seat in the output array.
        final_order[next_seat] = children[seat];
    }

    return final_order
}

console.log(get_final_order([1,2,3,4,5], 2));