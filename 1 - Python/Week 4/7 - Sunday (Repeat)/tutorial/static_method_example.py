#Static method
class Year:
    @staticmethod
    def is_leap(year):
        """ is_leap is a static method, doesn't depend on any instance
        specifica data. It is an utility funtion.
        Check if the year is a leap year
        % is for modulo
        """
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return True
        else:
            return False

year = int(input("Please input the year"))       

if Year.is_leap(year):
    print(f"{year} is a leap year")
else:    
    print(f"{year} is not a leap year")