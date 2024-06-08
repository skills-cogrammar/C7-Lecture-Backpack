// For each child, check if there is an open seat to the right 
// if there is no open seat to the right, make the child in the next 
// seat stand up so that the current child can take the seat
// any standing children will take priority to get a seat
// the last child will move to the first position.
function get_final_order(children, moves){
    let standing = undefined // There are no children standing initally

    for (let i = 0; i < moves; i++){ // We will move the children forward
        for (let seat = 0; seat < children.length; seat++){ // We will iterate through the chlidren
            let child = children[seat] // Set the child who is currenly being looked at
            
            // If there is a child standing, give them priority
            if (standing){ 
                child = standing;
            }

            // If we have reached the last seat 
            // We will need to move the child to the first open seat on the 
            // far left
            if ((seat + 1) == children.length){
                children[0] = child
                break
            }

            // Swap the stnading child and the current child
            // So that the child who is currently standing will take the seat
            // and the child in the next seat will stand and have priority in the 
            // next iteration
            standing = children[seat + 1]
            children[seat + 1] = child        
        }
    }

    return children
}


console.log(get_final_order([1,2,3,4,5], 2)) // [5,4,1,2,3]