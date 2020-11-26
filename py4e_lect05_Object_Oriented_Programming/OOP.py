# object-oriented programming example

# class is the template for making PartyAnimal object
class PartyAnimal:
    # Each PartyAnimal object has a bit of data
    x = 0
    # Each PartyAnimal object has a bit of code: method
    def party(self):
        self.x = self.x + 1 #self.x is variable, x start from 0
        print("So far",self.x)

# constuct a PartyAnimal object and store in an
# make object with template
an = PartyAnimal()

# PartyAnimal.party(an)

# call party method
an.party()
an.party() # an is alias of self
# 위랑 아래가 똑같음
# PartyAnimal class에서 party method를 불러오고 첫 번째 param으로 an instance를 사용
PartyAnimal.party(an) # self is alias of an

# .은 instance/object 내부를 들여다보는 도구라고 생각할 수 있음
# 위에서 3번 호출해서 x: 0->3 이 되었기 때문에
# an.x 는 이제 3이 되어 있음 (처음 template에서 x는 variable이고 self는 instance 내부에서 an의 alias)
print(an.x)

# type, dir을 통해서 알아볼 수 있음
x = list()
print(type(x))
print(dir(x))
