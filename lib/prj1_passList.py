import string
from random import *
def passls1(min,max,self):
    for i in range(self):
        char=string.ascii_lowercase + string.hexdigits + string.octdigits + string.ascii_uppercase 
        password="".join(choice(char) for x in range(randint(min,max)))
        print(password)
        
def passls2(min,max,self):
    for i in range(self):
        char= string.ascii_lowercase + string.ascii_uppercase + string.ascii_letters + string.punctuation
        password="".join(choice(char) for x in range(randint(min,max)))
        print(password)
        
def passls3(min,max,self):
    for i in range(self):
        char = string.digits + string.hexdigits + string.octdigits
        password = "".join(choice(char) for x in range(randint(min,max)))
        print(password)
