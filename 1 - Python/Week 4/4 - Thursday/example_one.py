# What makes up classes ? Our Pseudocode
"""
# Attributes
size - small, medium or large
colour - white, blue, red 
number of rooms - 2 - 10
type of flooring - hardwood, carpet or tile
"""

"""
# Methods
opening doors - open a door in house
turning on lights - this will turn on lights in house
cleaning - clean the house
"""

"""
Objects will be referred to as instances, these would be the houses the built
of the blueprint provided.
"""


class HousePlan:
    """
        This Python class initializes a house object with specified attributes and includes methods for
        opening the door, turning on the light, and cleaning with a robotic vacuum.
        
        :param u_size: The `u_size` parameter in the `__init__` method of your class seems to represent
        the size of the house. This could be the total area of the house, the number of square
        feet/meters, or any other measurement that indicates the physical size of the house
        
        :param u_colour: seems to represent the colour of the house. It is used to initialize the `colour`
        attribute of an object of this class
        
        :param u_num_rooms: The parameter `u_num_rooms` in the `__init__` method of the class seems to
        represent the number of rooms in a house or a building. It is used to initialize the `num_rooms`
        attribute of an object of this class
        
        :param u_floor: The `u_floor` parameter in the `__init__` method of the class is used to 
        represent the floor type of a building or house where the object is located. It is used to
        initialize the `floor` attribute of the object with the value passed to it when an instance of
        the class is
        """
    def __init__(self, u_size, u_colour, u_num_rooms, u_floor):
        self.size = u_size
        self.colour = u_colour
        self.num_rooms = u_num_rooms
        self.floor = u_floor

    def openDoor(self):
        """
        The function `openDoor` prints a message indicating that the door has been opened.
        """
        print("The door has been opened.")

    def lightSwitch(self):
        """
        The function `lightSwitch` prints a message indicating that the light has been turned on.
        """
        # NOTE: we can add conditional to check light status
        print("Light has been turned on.")

    def RumbaClean(self):
        """
        The function `RumbaClean` prints a message indicating that the house has been cleaned by
        Eufy-chan.
        """
        print("Eufy-chan has claimed that the house has been cleaned.")


# The code snippet you provided is taking user input to gather preferences for a house. Each `input`
# function prompts the user with a question and waits for the user to enter a response. Here's what
# each line is doing:
h_size = input("What size house would you prefer (small, medium, large): ")
h_colour = input("What color would you like the house in ? (blue, red, emereld): ")
h_num_rooms = int(input("How many rooms would you prefer (enter an integer value) : "))
h_flooring = input("What type of flooring would you like ? (wood, tile, carpet): ")

# The lines `kitt_house = HousePlan(h_size, h_colour, h_num_rooms, h_flooring)` and `kola_house =
# HousePlan("large", "green", 4)` are creating instances of the `HousePlan` class.
kitt_house = HousePlan(h_size, h_colour, h_num_rooms, h_flooring)
kola_house = HousePlan("large", "green", 4)

# This particular `print` statement is using an f-string in Python to format and display information
# about the `kitt_house` instance of the `HousePlan` class. Here's a breakdown of what it does:
print(f"""
      \n=============================================
      Size: {kitt_house.size}
      Colour: {kitt_house.colour}
      Number of rooms: {kitt_house.num_rooms}
      Type of flooring: {kitt_house.floor}
      \n=============================================
""")

kitt_house.openDoor()
print("\n=============================================")
kitt_house.lightSwitch()
print("\n=============================================")
kitt_house.RumbaClean()
print("\n=============================================")
