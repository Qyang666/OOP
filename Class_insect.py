import random

class Insect():
    def __init__(self):
        self.wings=2
        self.legs=4
        self.mile_length=0

    def mile_length(self):
        self.mile_length=random.randint(0,10)
        
        
    def return_miles(self):
        return self.mile_length
    



fly= Insect()
fly.mile_length()
print()