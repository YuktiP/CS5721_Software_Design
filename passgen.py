import string
from random import *
import datetime
from datetime import date

#from passgen import Rand_Pass and invoke an object of it 
class Randpass:

    def passGen(self):
        punc='@'
        punc1='_'
        punc2='*'
        self.characters = string.ascii_letters+ string.digits+punc+punc1+punc2
        #for i in range(0,10):
        self.password =  "".join(choice(self.characters) for x in range(randint(6,8)))
        #return(self.password)
        return(self.password)

    def pinGen(self):
        self.pingenerated= "".join(choice(string.digits) for x in range(randint(4,4)))
        #print(self.pingenerated)
        return(self.pingenerated)

    def cardGen(self):
        self.cardNo= "".join(choice(string.digits) for x in range(randint(16,16)))
        #print(self.pingenerated)
        return(self.cardNo)

    def cardExp(self):
        sysdate=date.today()
        expyear=sysdate.year+4
        expday=sysdate.day
        expmon=sysdate.month
        self.expiry=str(expyear)+'-'+str(expmon)+'-'+str(expday)
        return(self.expiry)       

    def accGen(self):
        self.accNo= "".join(choice(string.digits) for x in range(randint(8,8)))
        #print(self.pingenerated)
        return(self.accNo)

    def userGen(self):
        self.userId="".join(choice(string.digits) for x in range(randint(6,6)))
        return(self.userId)