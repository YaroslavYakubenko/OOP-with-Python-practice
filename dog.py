from animal import *

class Dog(Animal):
    def __int__(self, name, age, weight, breed='Terrer', color='White'):
        super().__init__(name, age, weight)
        self.breed = breed
        self.color = color

    def is_barking(self):
        print(f'{self.name} is barking')

    def create_dog(self):
        print(f'We created dog')