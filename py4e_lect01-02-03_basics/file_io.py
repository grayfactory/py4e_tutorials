'''
# line의 마지막에 붙는 \n 줄바굼은 white space로 간주되기 때문에 strip 하면 삭제됨
for line in fhand:
    line = line.rstrip()
    if line.startswith('From: '):
        print(line)
# 이 방식이 더 좋다고 할 수 있음, 실제 for loop 속에서 실행되는 것만 돌고
# if not은 돌지 않도록
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From: '):
        continue
    print(line)
'''
# Assignment 7.1
# file open
# fname = 'words.txt'
'''
try :
    fname = 'words.txt'
except:
    print('invaild file name')
    quit()

fh = open(fname)
for line in fh:
    print(line.upper().rstrip())
'''
# Assignment 7.2
# file open
fname = 'mbox-short.txt'
fh = open(fname)
cnt = 0
nval = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    cnt = cnt + 1
    spos = line.find(' ')
    sval = float(line[spos+1:])
    nval = nval + sval
    print(line)
print('Average spam confidence: ',nval/cnt)
