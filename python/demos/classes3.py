class People():
    def __init__(self, name, age, phone):
        self.name = str(name)
        self.age = int(age)
        self.phone = str(phone)

    def display_people(self):
        print(f"\nNAME: {self.name}")
        print(f"AGE: {self.age}")
        print(f"PHONE: {self.phone}")



def main():
    name = str(input("what is your name: "))
    age = int(input("what is your age: "))
    phone = str(input("what is your phone number: "))

    x = People(name, age, phone)


    print(x.display_people())



main()
