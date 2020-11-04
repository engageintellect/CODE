

class Peeps():
    def __init__(self, name, age, fav_foods):
        self.name = name
        self.age = age
        self.fav_foods = fav_foods

    def display(self):
        print(self.name, self.age)

        for x in self.fav_foods:
            print(x)


x = Peeps("jim", 33, ["ice-cream", "pizza", "cake"])
x.display()
