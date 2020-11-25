hrs = input("Enter Hours:")
rph = input("Enter rate:")

try :
    ihrs = float(hrs)
    irph = float(rph)
except :
    ihrs = -1

if ihrs == -1:
    print("not a number")
elif ihrs <= 40:
    pay = ihrs * irph
else :
    intimepay = 40 * irph
    ovtimepay = (ihrs - 40) * (irph * 1.5)
    pay = intimepay+ovtimepay

print(pay)
