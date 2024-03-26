

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


class Car(Vehicle):

    def __init__(self, brand, price, color, model):
        super().__init__(brand, price, color, model)

    def Move(self):
        print(f'A {self.color} {self.brand} {self.model} is moving away.')


class Aeroplane(Vehicle):
    
    def __init__(self, brand, price, color, model):
        super().__init__(brand, price, color, model)

    def Move(self):
        print(f'A {self.color} {self.brand} {self.model} is flying away.')


boeng = Aeroplane('Boeng', 'R100000', 'White', '747')
boeng.Move()

bmw = Car('BMW', 'R25000', 'Grey', 'X5')
bmw.Move()