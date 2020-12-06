import string
from random import *

#from passgen import Rand_Pass and invoke an object of it 
class Rand_Pass:

    def passgen(self):
        punc='@'
        punc1='_'
        punc2='*'
        self.characters = string.ascii_letters+ string.digits+punc+punc1+punc2
        for i in range(0,10):
            self.password =  "".join(choice(self.characters) for x in range(randint(6,8)))
            print(self.password)

r=Rand_Pass()
r.passgen()        