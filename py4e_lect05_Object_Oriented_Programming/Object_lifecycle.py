# class with constructor

class PartyAnimal:
    x = 0

    def __init__(self): # 인스턴스가 생성되면서 실행되는 부분
        print('i am constructed')

    def party(self):
        self.x = self.x + 1
        print("so far", self.x)

    def __del__(self): # 인스턴스가 사라지면서 실행되는 부분
        print("i am distructied", self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42

print("============\n\n\n")

# Constructor는 추가 parameters를 가질 수 있고, parameter들은
# 같은 class로 찍어내는 개별 instance들의 variable로 사용될 수 있음

class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z): # parameter 추가
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

s = PartyAnimal("gray")
s.party()

j = PartyAnimal("Park")
j.party()
s.party()
