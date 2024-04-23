students = ["Zahra", "Moumita", "Anri", "Julien"]

def passNote (destination):
    found = False
    i = 0

    while (not found):
        if (i == len(students)):
            return "Destination not found"
        elif (destination == students[i]):
            found = True
            return "Note delivered"
        
        i += 1




