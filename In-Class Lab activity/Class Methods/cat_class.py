class Cat:
    def __init__(self):
        self.color = ""
        self.name = ""
        self.weight = 0

    def meow(self):
        print("Meow!")


my_cat = Cat()
my_cat.name = "Fluffy"
my_cat.color = "black"
my_cat.weight = 5

print("My cat's name is " + my_cat.name + ".")
print("What does " + my_cat.name + " say?")
my_cat.meow()


