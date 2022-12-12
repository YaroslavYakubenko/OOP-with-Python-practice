from animal import *
from dog import *
from cat import *
from gibrid import *

animal = Animal(name='Tuzik', weight=10, age=2)
print(animal.__dict__)
# animal.print_info()

dog1 = Dog('Barbos', 5, 10)
dog1.create_dog()
print(dog1.__dict__)

dog1.print_info()
dog1.is_barking()
# dog1.color

cat1 = Cat('Vasya', 12, 10)
# print(cat1.__dict__)
cat1.create_cat()
print(cat1.__dict__)


# cat2 = Cat('Georgiy')
# print(cat2.name)

gibrid = Gibrid('Puch', 12, 25)
# gibrid.print_create()
# print(gibrid.__dict__)