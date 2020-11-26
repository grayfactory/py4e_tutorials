from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

url = 'http://www.dr-chuck.com/page1.htm'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# a는 앵커 tag를 찾음
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))

print(tag)


# exsample 2
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://www.dr-chuck.com'
html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href',None))


'''
Assignment with BeautifulSoup

Scraping Numbers from HTML using BeautifulSoup In this assignment you will write
a Python program similar to http://www.py4e.com/code3/urllink2.py.
The program will use urllib to read the HTML from the data files below, and parse the data,
extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment.
One is a sample file where we give you the sum for your testing and the other is the actual data you need
to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1077025.html (Sum ends with 58)
You do not need to save these files to your folder since your program will read the data directly from the URL.
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
'''
import re
print('Assignment\n\n')
url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')

# version 1 regex
tmp = 0
for tag in tags:
    # print(tag)
    num = re.findall('[0-9]+',tag.decode())
    tmp = tmp + int(num[0])
    # print(tmp)

# version 2 regex & list comprehension
# tags = soup('span')
# 이 경우에 decode는 list가 아닌 single string일 때 전체를 decode 하기 때문에
# BeautifulSoup 하고는 궁합이 잘 맞지 않는다고 할 수 있겠다
# 그리고 답이 다른것으로 봐서 어딘가 맞지 않는 html 구문이 있는 것 같음
print( sum([int(num) for num in re.findall('[0-9]+', html.decode()) ]) )


# version 3 BeautifulSoup function
url = 'http://py4e-data.dr-chuck.net/comments_1077025.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# soup.select로 'span' tag가 있는 부분을 list로 돌려 받을 수 있음
tmp = sum([ int(ff.get_text()) for ff in soup.select('span')])
print(tmp)

'''
Assignment with BeautifulSoup 2

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1).
Follow that link. Repeat this process 4 times.
The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah

Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Aled.html
Find the link at position 18 (the first name is 1).
Follow that link. Repeat this process 7 times.
The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: F

'''
print('Assignment 2 \n\n\n')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Aled.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup.select('a')
pos = 18-1
count = 7
for cnt in range(count):
    Retrieve = tags[pos].get('href',None)
    print(f'Retrieving: {Retrieve}')
    html = urllib.request.urlopen(Retrieve, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.select('a')
