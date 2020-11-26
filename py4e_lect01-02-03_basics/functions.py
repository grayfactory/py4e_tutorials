def computepay(h,r):
    if h > 40:
        overpay = (h-40) * (r*1.5)
        norpay = 40*r
        return overpay+norpay
    else :
        return h*r

# hrs = input("Enter Hours:")
# rph = input("Enter Rate:")
hrs = 45
rph = 10.50
try :
    ihrs = float(hrs)
    irph = float(rph)
except :
    print('not a number')

p = computepay(ihrs,irph)
print("Pay",p)
