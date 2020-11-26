# Assignment를 list와 다르게 할 수 있음
(x,y) = (4,'gray')
print(x,y)

# 위를 활용해서 dict.items()로 응용을 하는 것
stuff = dict()
stuff['name'] = 'gray'
stuff['age'] = 32
for k,v in stuff.items():
    print(k,v)

# tuple은 서로 비교가 가능
vals = (0,1,2) < (5,1,2)
print(vals)
# 순차적으로 비교해 나감
vals = (0,1,2000) < (0,3,2)
print(vals)

# 비교를 이용해서 sorted할 수 있음
d = {'a':10,'b':1,'c':22}
# sorted 된 list를 받을 수 있음, sorted의 기준은 key값으로 하게됨
t = sorted(d.items())
print(t)
# 이렇게 해서 dict 속에서 sorted 된 순서로 iter할 수 있게됨
for k,v in sorted(d.items()):
    print(k,v)
# 만약세 valuse로 sorted하고 싶으면
# value - key tuple을 만들어서 하면되겠음

tmp = list()
for k,v in d.items():
    tmp.append( (v,k) )
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)


# now top 10 most common words
fhand = open('py4e_lect01-02-03_basics/romeo.txt')
counts = dict()

for lines in fhand:
    words = lines.rstrip().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
# 여기서부터 끝까지 list comprehension으로 한줄에 할 수 있음

print('list comprehension: ', sorted( [(v,k) for k,v in counts.items()] ))

print(counts)
nlist = list()
for k, v in counts.items():
    nlist.append( (v, k) )

nlist = sorted(nlist, reverse=True)
print(nlist[:10])

[(v,k) for k,v in counts.items()]



print('\n\n\n\n')
'''
Assigment 10.2
10.2 Write a program to read through the mbox-short.txt
and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time
and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated
the counts for each hour, print out the counts, sorted by hour as shown below.
'''
name = "py4e_lect01-02-03_basics/mbox-short.txt"
handle = open(name)
cnts = dict()
for lines in handle:
    if 'From ' not in lines: continue
    # print(lines.rstrip().split()[5][:2])
    hr = lines.rstrip().split()[5][:2]
    cnts[hr] = cnts.get(hr,0)+1
# print(cnts)

# print(sorted([(key,vals) for key,vals in cnts.items()]))
sorted_cnts = sorted([(key,vals) for key,vals in cnts.items()])
for key, vals in sorted(cnts.items()):
    print(key, vals)

ss = -1
if ss is None:
    print('a')
