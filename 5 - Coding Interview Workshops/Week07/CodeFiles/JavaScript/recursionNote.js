let students = ["Zahra", "Moumita", "Anri", "Julien"];

function passNote (destination, location) {
    if (location == len(students))
        return "Destination not found";
    else if (destination == students[location])
        return "Note delivered!";
    else
        return passNote(destination, location + 1);
}

