class Dog:
    def __init__(self, name):
        self.name = name
        self.trick_list = []

    def get_name(self):
        return self.name

    def sit(self):
        print(self.name, "sits")
        self.trick_list.append("sit")

    def lay_down(self):
        print(self.name, "lays down.")
        self.trick_list.append("lay down")

    def roll_over(self):
        print(self.name, "rolls over.")
        self.trick_list.append("rolls over")

    def print_trick_list(self):
        if not self.trick_list:
            print(self.name, "has not performed any tricks yet.")
        else:
            print(self.name, "has performed the following tricks:")
            for trick in self.trick_list:
                print(trick)


    def __str__(self):
        return f"Dog(name={self.name}, tricks={self.trick_list})"
    '''
    The "f" at the beginning of a string in Python denotes an f-string, 
    which stands for formatted string literals. F-strings allow you 
    to embed expressions inside string literals, using curly braces {}.
    '''


dog1 = Dog("Spot")
dog1.sit()
print(dog1)
dog1.lay_down()
dog1.roll_over()
dog1.print_trick_list()

