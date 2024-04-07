class Avengers:
    """
    total_avengers is a class variable to keep track
    of the total number of avengers
    """
    total_avengers = 0

    def __init__(self,name):
        """
        total_avengers: Increment of the total no. of avengers 
        when a new Avenger instance is created.
        """
        self.name = name
        Avengers.total_avengers += 1

    @classmethod
    def display_total_avengers(cls):
        print("The total number of Avengers: ", cls.total_avengers)

#Creates instances of the class Avengers
avenger1 = Avengers("Captain America")
avenger2 = Avengers("Iron Man")
avenger3 = Avengers("Black Widow")

#Calling the class method to display the total number of Avengers
Avengers.display_total_avengers()