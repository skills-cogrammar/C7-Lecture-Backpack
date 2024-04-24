# ==================== Multidimensional Lists demo ====================
"""
Let's create an example of a multidimensional list representing 
a seating arrangement in a theatre. We'll consider a theatre with rows and columns, 
and each seat will be represented by a tuple containing the row number and 
the seat number within that row. We'll also include functionality to check the 
availability of seats, reserve seats, and display the seating arrangement.
"""
# from tabulate import tabulate

class Theatre:
    def __init__(self, rows, seats_per_row):
        # Initialize the theatre with the given number of rows and seats per row
        self.rows = rows
        self.seats_per_row = seats_per_row
        # Create a 2D list to represent the seating arrangement, 
        # initially all seats are None (empty)
        # For each row create a list of [None] * seats_per_row
        self.seating_arrangement = [[None] * seats_per_row for _ in range(rows)]

    def is_seat_available(self, row, seat):
        # Check if a seat at the specified row and seat number is available
        # Return True if a seat value is None else return False
        return self.seating_arrangement[row][seat] is None

    def reserve_seat(self, row, seat, customer_name):
        # Reserve a seat for a customer at the specified row and seat number
        if self.is_seat_available(row, seat):
            # If the seat is available, reserve it by assigning the customer's name to the corresponding position in the seating arrangement
            self.seating_arrangement[row][seat] = customer_name
            print(f"Seat {row}-{seat} reserved for {customer_name}")
        else:
            # If the seat is already taken, inform the customer
            print(f"Seat {row}-{seat} is already taken")

    def display_seating_arrangement(self):
        # Display the current seating arrangement of the theatre
        for row_number, row in enumerate(self.seating_arrangement):
            row_display = ""
            for seat_number, customer_name in enumerate(row):
                if customer_name is None:
                    # If the seat is empty, display "[#]"
                    row_display += f"  [ {seat_number} ]  "
                else:
                    # If the seat is reserved, display "[customer_name]"
                    row_display += f"  [{customer_name}]  "
            print(f"Row {row_number + 1}:{row_display}")

    # Explore the tabulate function to create a better display for 2D Lists
    # pip install tabulate is required to import tabulate
            
    # def display_seating_arrangement(self):
    #     table = []
    #     for row_number, row in enumerate(self.seating_arrangement):
    #         row_display = []
    #         for seat_number, customer_name in enumerate(row):
    #             if customer_name is None:
    #                 row_display.append("[ ]")
    #             else:
    #                 row_display.append(f"[{customer_name}]")
    #         table.append(row_display)
    #     print(tabulate(table, headers=[f"Seat {i}" for i in range(1, self.seats_per_row + 1)], 
    #                    showindex=[f"Row {i}:" for i in range(1, self.rows + 1)], tablefmt="simple"))

# Creating a theatre with 10 rows and 8 seats per row
theatre = Theatre(rows=10, seats_per_row=8)

# Reserving some seats
theatre.reserve_seat(3, 4, "Alice")
theatre.reserve_seat(3, 5, "Bob")
theatre.reserve_seat(5, 6, "Charlie")

# Displaying the seating arrangement
print("\nSeating Arrangement:")
theatre.display_seating_arrangement()

""" Prep for below calendar example:
# Multidimensional Dictionary
my_staff = {managers: {top: ["John", "Mary"], 
                        mid: [], 
                        entry: []}, 
            employees: {junior: ["Andrew", "Alice", "Daisy"], 
                        senior:[]}}
print(my_staff[employees][junior][2])      #Output: Daisy

# Index out of range error handling
my_list = [1, 2, 3, 4, 5]

try:
    index = 6  # Index out of range
    value = my_list[index]  # Try to access element at index
except IndexError:
    # Handle the specific exception (IndexError)
    print(f"Error: Index {index} is out of range.")  # Print error message
else:
    # Execute if no exceptions were raised
    print(f"Value at index {index}: {value}")  # Print value at index
    """
"""
Define a Calendar dictionary with functions to add and display events for 
a specific month. Use a nested dictionary structure to store events, 
where the keys represent the year, month, and day, and the values are 
lists of events for that day.

# Note: The only difference in the nested dictionary or nested list implementation
#       is the use of a key instead of an index number.

The add_event function allows users to add events by specifying 
the year, month, and day, along with the event description.
The display_month function displays events for a specific month and year. 
If no events are found for the given month and year, 
it prints a message indicating that there are no events.
"""
def add_event(calendar, year, month, day, event):
    if year not in calendar:
        calendar[year] = {}
    if month not in calendar[year]:
        calendar[year][month] = {}
    if day not in calendar[year][month]:
        calendar[year][month][day] = []
    calendar[year][month][day].append(event)

def display_month(calendar, year, month):
    print(f"Month: {month}, Year: {year}")
    if year in calendar and month in calendar[year]:
        for day, events in calendar[year][month].items():
            print(f"Day {day}: {events}")
    else:
        print("No events for this month.")

# Creating an empty calendar
calendar = {}

# Adding events to the calendar
add_event(calendar, 2024, 1, 9, "Work Meeting on January 9th")
add_event(calendar, 2024, 1, 9, "Take a lunch break")
add_event(calendar, 2024, 2, 3, "Dentist Appointment on February 3rd")

# Displaying the calendar for January 2024
display_month(calendar, 2024, 1)

# Displaying the calendar for February 2024
display_month(calendar, 2024, 2)

#===============  BONUS: OOP Version of the Calendar  =============== 

class Calendar:
    def __init__(self):
        self.calendar = {}

    def add_event(self, year, month, day, event):
        if year not in self.calendar:
            self.calendar[year] = {}
        if month not in self.calendar[year]:
            self.calendar[year][month] = {}
        if day not in self.calendar[year][month]:
            self.calendar[year][month][day] = []
        self.calendar[year][month][day].append(event)

    def display_month(self, year, month):
        print(f"Month: {month}, Year: {year}")
        if year in self.calendar and month in self.calendar[year]:
            for day, events in self.calendar[year][month].items():
                print(f"Day {day}: {events}")
        else:
            print("No events for this month.")

# Creating a calendar instance
calendar = Calendar()

# Adding events to the calendar
calendar.add_event(2024, 1, 9, "Work Meeting on January 9th")
calendar.add_event(2024, 1, 9, "Take a lunch break")
calendar.add_event(2024, 2, 3, "Dentist Appointment on February 3rd")

# Displaying the calendar for January 2024
calendar.display_month(2024, 1)

# Displaying the calendar for February 2024
calendar.display_month(2024, 2)
