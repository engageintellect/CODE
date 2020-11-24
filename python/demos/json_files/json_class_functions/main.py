import json


class People:
    def __init__(self, name, age, food):
        self.name = name
        self.age = age
        self.food = food
    
    def mkdict(self):
        mydict = {'name': self.name,
                'age': self.age, 
                'food': self.food}
        
        return mydict



def write_json():
    with open ('myfile.json', 'w') as f:
        json.dump(x.mkdict(), f)

def read_json():
    with open ('myfile.json', 'r') as f:
        data = json.load(f)
        return data




x = People('josh', 32, ['pizza', 'cheese'])
write_json(); print(read_json())



