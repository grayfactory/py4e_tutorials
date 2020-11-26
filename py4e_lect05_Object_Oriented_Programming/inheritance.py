'''
Class: a template
Attibute: a variable within a class
Method: a function within a class
Object: a particular instance of a class
Constructor: code that runs when an object is created
Inheritance: the ability to extend a class to make a new class
'''
# Inheritance, Class-Subclass
class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z): # parameter 추가
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

class FootballFan(PartyAnimal): # PartyAnimal을 상속받음
    point = 0
    def touchdown(self):
        self.point = self.point + 7
        self.party() # touchdown 호출하면 상속받은 PartyAnimal의 method도 호출
        print(self.name, "point", self.point)

s = PartyAnimal("gray")
s.party()

j = FootballFan("Park")
j.party()
j.touchdown()
