class Monster1:
    def __init__(self):
        self.name = ""
        self.health = 0

    def decrease_health(self, amount):
        self.health -= amount



kong = Monster1()
kong.name = "Kong"
kong.health = 90
print(kong.name + " has health of " + str(kong.health))
kong.decrease_health(40)
print(kong.name + " has health of " + str(kong.health))