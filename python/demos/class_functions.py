class Rectangle():
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def rect_area(self):
        return self.height * self.width

    def rect_perimeter(self):
        return self.height * 2 + self.width * 2




def main():
    x = Rectangle(10,50)
    y = Rectangle(25,50)
    z = Rectangle(38,92)

    print(f"X [PERIM: {x.rect_perimeter()} AREA: {x.rect_area()}]")
    print(f"Y [PERIM: {y.rect_perimeter()} AREA: {y.rect_area()}]")
    print(f"Z [PERIM: {z.rect_perimeter()} AREA: {z.rect_area()}]")


main()

