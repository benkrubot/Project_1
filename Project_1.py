# I tested whether entering 1 or 0 would change the state of the engine/radio/window.
# Also tested whether the loops worked to ensure that the user entered the correct input,
# as well as if entering Yes exited the program, or if entering No looped back to the beginning.

class car:
    def __init__(self):
        self.__engine = 1
        self.__radio = 1
        self.__window = 1  # what has been played already

    def get_engine(self):
        if x == 1:
            self.__engine == 1
            print("\nThe engine is purring.")
        elif x == 0:
            self.__engine == 0
            print("\nThe engine is off.")

    def get_radio(self):
        if x == 1:
            self.__radio == 1
            print("\nSome tunes are playing.")
        elif x == 0:
            self.__radio == 0
            print("\nThe radio is off.")

    def get_window(self):
        if x == 1:
            self.__window == 1
            print("\nFresh air is filling the car.")
        elif x == 0:
            self.__window == 0
            print("\nThe window is closed.")


newcar = car()
print("You get inside your car.")

while True:
    x = int(input("\nEnter 1 to turn the car on, 0 to turn it off: "))
    while x < 0 or x > 1:
        x = int(input("\nPlease enter 1 or 0: "))
    else:
        newcar.get_engine()

    x = int(input("\nEnter 1 to turn on the radio, 0 to turn it off: "))
    while x < 0 or x > 1:
        x = int(input("\nPlease enter 1 or 0: "))
    else:
        newcar.get_radio()

    x = int(input("\nEnter 1 to roll down the window, 0 to close it: "))
    while x < 0 or x > 1:
        x = int(input("\nPlease enter 1 or 0: "))
    else:
        newcar.get_window()

    y = input("\nWould you like to quit? ")
    while y != "No" and y != "no" and y != "Yes" and y != "yes":
        y = input("\nPlease try again: ")
    else:
        if y == "No" or y == "no":
            True
        elif y == "Yes" or y == "yes":
            print("\nGoodbye.")
            break