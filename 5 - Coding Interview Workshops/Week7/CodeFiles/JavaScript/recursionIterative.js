let students = ["Zahra", "Moumita", "Anri", "Julien"];

function passNote (destination){
    let found = False;
    i = 0;

    while (!found){
        if (i == len(students))
            return "Destination not found";
        else if (destination == students[i]){
            found = True;
            return "Note delivered";
        }
        
        
        i += 1;
    }
}


