counts = dict()
names = ['a','b','c','c','d','a']
for name in names:
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

# idiom of dictionaries
# retieve/create/update & counts
for name in names:
    # get 은 dict에서 key가 존재하면 value를 가지고 오고
    # 만약 해당 key가 없으면, 2번째 param의 default return한다.
    # 아래 줄 같은 경우는 counts에서 name key가 없으면 defaults 0을 return해서
    # counts[name]에 할당하는것
    counts[name] = counts.get(name, 0) + 1
print(counts)

for key in counts:
    print(key, counts[key])

# list로 만들면 key만 조회
print(list(counts))
print(counts.keys())
# value만 조회
print(counts.values())
# key-value를 묶어서 tuple 형태로 한완
print(counts.items())

# key와 value를 for loop에서 각각 iter 변수에 할당 할 수 있음!
# enumerate같은것
for k,v in counts.items():
    print(k,v)


# final code
handle = open('words.txt')
wcnt = dict()
for line in handle:
    words = line.split()
    for word in words:
        wcnt[word] = wcnt.get(word,0) + 1

bigcnt = None
bigword = None
for word,cnt in wcnt.items():
    if bigcnt == None or bigcnt < cnt:
        bigcnt = cnt
        bigword = word
print(bigword, bigcnt)

stuff = dict()
print(stuff.get('candy',-1))
print(stuff)


# Assignment 9.4
handle = open('mbox-short.txt')
ecnt = dict()
for lines in handle:
    if 'From ' not in lines: continue
    # print(lines.rstrip())
    whos = lines.rstrip().split()[1]
    ecnt[whos] = ecnt.get(whos,0) + 1

# print(ecnt)
fcnt = None
fwho = None
for k,v in ecnt.items():
    if fcnt == None or fcnt < v:
        fcnt = v
        fwho = k
print(fwho, fcnt)
