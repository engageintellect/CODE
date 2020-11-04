

class People():
    def __init__(self, name, age, fave_food):
        self.name = name
        self.age = age
        self.fave_food = fave_food

    def display(self):
        print(self.name, self.age, self.fave_food)



def Get_Info():
    name = input("Enter name: ")
    age = input("Enter age: ")
    fave_food = []

    fave_food[0] = input("first fav food: ")
    fave_food[1] = input("2nd fav food: ")
    fave_food[2] = input("3rd fav food: ")

    x = People(name, age, fave_foods)
    x.display()




Get_Info()


