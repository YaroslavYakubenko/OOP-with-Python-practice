from animal import *


class Cat(Animal):

    def __int__(self, name, age, weight, color_eyes='Blue'):
        super().__init__(name, age, weight)
        self.color_eyes = color_eyes

    def print_info(self):
        print(f'Cat is {self.name} with weight {self.weight} kg and age {self.age} years.')

    def create_cat(self):
        print(f'We created a cat, her name is {self.name}')