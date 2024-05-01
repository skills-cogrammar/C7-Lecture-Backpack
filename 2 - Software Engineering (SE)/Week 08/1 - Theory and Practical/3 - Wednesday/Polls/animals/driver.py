###############################################
#                                             #
#  Please don't modify this script. It works  #
#                                             #
#  This is the driver script                  #
#                                             #
#  Run it as follows: python driver.py        #
#                                             #
###############################################

from cat import Cat
from dog import Dog

dog_1 = Dog("Rocky", 5)
cat_1 = Cat("Charlie", 3)

if __name__ == "__main__":

    print(f"Dog 1: {dog_1}")
    print(f"Cat 1: {cat_1}")

    dog_1.get_name()
    cat_1.get_name()

    print(dog_1.sleep())
    print(cat_1.sleep())

    print(dog_1.make_sound())
    print(cat_1.make_sound())


