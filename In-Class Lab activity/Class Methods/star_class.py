class Star:
    def __init__(self, name):
        self.name = name
        print("A star is born! It's name is " + name)

    def get_name(self):
        print("The name of the star is " + self.name)


star1 = Star("Emily")
star2 = Star("Andromeda")
star1.get_name()
