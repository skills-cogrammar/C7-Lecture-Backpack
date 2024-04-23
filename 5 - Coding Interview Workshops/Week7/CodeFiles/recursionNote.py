students = ["Zahra", "Moumita", "Anri", "Julien"]

def passNote (destination, location):
    if (location == len(students)):
        return "Destination not found"
    elif (destination == students[location]):
        return "Note delivered!"
    else:
        return passNote(destination, location + 1)

