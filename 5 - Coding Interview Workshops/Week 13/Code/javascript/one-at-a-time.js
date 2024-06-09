//Have a temporary unit for setting the standing child (Set to undefined for the first time)
//Have a for loop that iterates according to the seats asked to move (breaks when no more moves are left)
    //Have a loop that iterates over the number of children(Breaks when the pointer exceeds no. of children)
        //pick the priority child (Use a variable to store priority child) (First child during the 1st iteration)
        //check if there is a standing child
            //(IF TRUE)=> set the standing child as priority
        //checking if the we've reached the last child
            //(IF TRUE)=> place the last child on the 1st position
        //Swap the stnading child and the current child




        
/**
 * 
 * @param {List} children -> Will have numbers to identify them
 * @param {Number} moves -> Number of seats each child should move
 * @returns {List} -> An arranged list according to the movement
 */
function getFinalOrder(children, moves){
    let standing = undefined // O(1)

    for (let i = 0; i < moves; i++){ // O(m)
        for (let seat = 0; seat < children.length; seat++){ // O(n)
    
            let child = children[seat] // O(1)
            
            // O(1)
            if (standing){  
                child = standing;
            }

            //
            if ((seat + 1) == children.length){ //O(n)
                children[0] = child //O(1)
                break //O(1)
            }

            // O(1)
            standing = children[seat + 1]
            children[seat + 1] = child        
        }
    }

    return children
}
//Drop constants
//EQ = O(m) * O(n) + O(n)
//EQ = O(m) * O(n) + O(n)
//EQ = O(mn)   // Pick the fastest growing
//EQ = O(mn) Time complexity => O(n)



console.log(getFinalOrder([1,2,3,4,5], 2)) // [4,5,1,2,3]