

class Vehicle():

    def __init__(self, brand, price, color, model):
        self.brand = brand
        self.price = price
        self.color = color
        self.model = model

    def Move(self):
        print(self.brand+ ' '+self.model + ' is moving.')
    
    def Features(self):
        print('The color is ',self.color,'and it costs ', self.price)


bmw = Vehicle('BMW', 'R2500', 'red', 'x5')
bmw.Move()
bmw.Features()
