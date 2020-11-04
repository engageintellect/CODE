class rect():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2








x = rect(50,10)
print(x.get_area())
print(x.get_perimeter())

    
