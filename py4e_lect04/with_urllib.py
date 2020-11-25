import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

for lines in fhand:
    print(lines.decode().strip())

# request.urlopen 하면 파일처럼 handle할 수 있음
# a href= "" -> 이 부분을 regex로 찾아서, 다시 urlopen 하면 해당링크를 클릭할 수 있음
