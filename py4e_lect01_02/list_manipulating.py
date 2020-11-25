# Assignment 8.4
fname = 'romeo.txt'
fh = open(fname)
lst = list()
for line in fh:
    wpicese = line.rstrip().split()
    for words in wpicese:
        if words not in lst:
            # print(words)
            lst.append(words)
            # print(lst)
lst.sort()
print(lst)

# Assignment 8.5
fname = 'mbox-short.txt'
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for fl in fh:
    if 'From ' not in fl: continue
    print(fl.split()[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
