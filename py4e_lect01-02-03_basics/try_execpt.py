hrs = input("Enter Hours:")
rph = input("Enter rate:")
# 되도록이면 trackback error를 만들지 않기 위해서
# 신뢰가 가지 않는 부분, 오류가 예상되는 부분에
# try ~ except을 활용해야한다.
try :
    ihrs = float(hrs)
    irph = float(rph)
except :
    ihrs = -1 # user input이 이상할때, -1을 넣고

if ihrs == -1: # 여기서 debug로 잡아낼 수 있다.
    print("not a number")
elif ihrs <= 40:
    pay = ihrs * irph
else :
    intimepay = 40 * irph
    ovtimepay = (ihrs - 40) * (irph * 1.5)
    pay = intimepay+ovtimepay

print(pay)
