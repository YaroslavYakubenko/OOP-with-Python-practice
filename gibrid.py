from cat import *
from dog import *

class Gibrid(Dog, Cat):
    def print_create(self):
        print(f'We created catdog')
