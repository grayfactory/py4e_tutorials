# type & method
stuff = '    Hello world     '
print(type(stuff))
print(dir(stuff))

a = stuff.strip()
print(a)
a = stuff.rstrip()
print(a)

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
# find 두번째 param 해당 index 부더 시작해서 찾기
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1:sppos]
print(host)

# Assignment 6.5
# 6.5 Write code using find() and string slicing (see section 6.10)
# to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475";
spos = text.find(' ')
print(float(text[spos:].strip()))
