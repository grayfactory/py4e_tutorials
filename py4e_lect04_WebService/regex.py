import re

# handle = open('mbox-short.txt')
'''
# ^ 시작점
# . 아무 문자
# * is any number of times 0을 포함
# + 는 적어도 1번, 0을 포함하지 않음

ex)
^X.*: --> ^(대문자 X로 시작해서), .(any 문자가), *(여러개 있고), :(마지막에 콜론으로 끝나는)
여기서 대문자 X와 :이 regex가 아니기 때문에 ^x 시작에서 :이 마지막이됨
X-Sieve: CMU sieve 2.3
X-DSPAM: Innocent
X-DSPAM: 0.231
X-Content-type-message-Body: text/plan
위와같은 형태의 문자열이 다 일치해서 찾아볼 수 있게됨

ex2)
X-Sieve: CMU sieve 2.3
X-DSPAM: Innocent
X-DSPAM: 0.231
X-Content type message Body: text/plan
위 예시에서 X-다음에 :콜론까지 공백이 없는 것만 찾아보고 싶다면
^X-\S+:
\S -> match any non-whitespace character 공백이 아닌 문자열
+  -> one or more times (적어도 1번은 나와야함)

ex3) [0-9]+
[0-9] -> 0-9범위의 숫자 1개
+     -> one or more
즉, 0-9범위의 숫자가 여러개 있는 패턴
[AURES] 와 같이 []속에 들어가있는 문자열을 지정해 줄 수도 있음, []속에 문자들 중 1개를 의미
'''
x = 'my 2 favorite number are 191 and 233'
y = re.findall('[0-9]+',x)
print(y)

'''
greedy matching
^F.+: 아래 예제에서 From: 까지만 일치시키고 싶지만, 뒤에 :콜론이 또 있어서
최대한 많이 포함시켜서 출력하게됨
+ or * 는 매우 greedy 하다.

'''
x = 'From: Using the: character' # From: (첫번째 콜론을 넘어서) the: (두번째 콜론까지 포함)
y = re.findall('^F.+:',x)
print(y)

'''
non-greedy matching
^F.+?:
? -> 이거를 붙여주면 not greedy 하게 찾는다 -> 마지막까지 찾지 않는다
'''
x = 'From: Using the: character'
y = re.findall('^F.+?:',x)
print(y)

'''
\S+@\S+
\S -> 공백이 아닌 문자
+ -> one or more
한 글자 이상의 공백이 아닌 문자 @문자가 있는 패턴
if
\S 뒤에 +가 붙지 않으면 greedy 하지 않기 때문에 @양쪽으로 한칸씩만 find
'''
x = 'From stephen.marquad@uct.ac.za sat jan 5 09:12:16 2008'
y = re.findall('\S+@\S+', x)
z = re.findall('\S@\S', x)
print(y, z)


'''
match 된 패턴에서 실제로 추출되는 영역을 ()괄호로 지정해 줄 수 있음
^From (\S+@\S+)
위와 동일하지만
^From 으로 시작하는 것 까지 포함해서 실제 추출은 메일주소 부분만 하게됨
'''
x = 'From stephen.marquad@uct.ac.za sat jan 5 09:12:16 2008'
y = re.findall('^From \S+@\S+', x)
z = re.findall('^From (\S+@\S+)', x)
print(y, z)

'''
지금까지 방법들
ex)도메인 주소만 뽑기
'''
# 1
x = 'From stephen.marquad@uct.ac.za sat jan 5 09:12:16 2008'
xpos = x.find('@')
print(xpos)
ypos = x.find(' ',xpos)
print(ypos)
print(x[xpos+1:ypos])

#2 split
s1 = x.split('@')[1].split(' ')[0]
print(s1)

# regex
# @([^ ]*) -> [^ ] everything but space []괄호는 글자 하나
# []괄호 속에 ^이게 처음에 오면 not의 의미
r1 = re.findall('@(\S+)',x)
r2 = re.findall('@([^ ]*)',x)
# more turn해서 From 으로 시작하는 것을 포함
r3 = re.findall('^From .*@([^ ]*)',x)
print(r1,r2,r3, sep='\n')


# X-DSPAM-Confidence: 0.998
# ^X-DSPAM-Confidence: ([0-9.]+)
# []괄호속에 0-9하고 .도 넣어줘야 부동소수점 표현에서 점이 포함되는 패턴이 됨



'''
만약 정규표현식에 할당된 $와 같은 문자를 실제 찾는 문자로 인식시키고 싶으면
앞에다 \를 붙여준다 \$와 같이
\$[0-9.]+ 이런식으로, $로 시작하는 숫자 패턴을 찾음
'''


# Assingment regular expression
fname = 'regex_sum_1074405.txt'
handle = open(fname)
sumofnum = 0
for lines in handle:
    line = lines.rstrip()
    numlist = re.findall('[0-9]+',line)
    if len(numlist) < 1: continue
    tmp = 0
    for ii in numlist:
        tmp = tmp + int(ii)
    sumofnum = sumofnum + tmp
print(sumofnum)

# 한줄에 가능하다고?
# print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
print('\n\n\n')

tmps = open(fname).read()

print(type(tmps))
tmps = sum( [ int(s) for s in re.findall('[0-9]+', open(fname).read())] )
print(tmps)
