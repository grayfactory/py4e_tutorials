'''
Tags: indicate the begainning and ending of elements
Attribute: Keyword/value pairs on the opening tag of XML
Serialize / De-Serialize: Convert data in one program into a
                          Common format that can be stored and/or transmitted between systems
                          in a programming language-independanct manner

- example of XML
<person>                Start tag
    <name>Chuck</name>
    <phone type="intl"> Attribute Keyword:"value"
    +10 3444 6916       Text Content
    </phone>            end tag
    <email hide="yes"/> Self Closing tag, 모든 필요한 정보가 Attribute에 포함되어서 text content가 필요없음
</person>               end tag

- XML as a Tree && XML Text and Attribute
<a>
    <b w='5'>X</b>
    <c>
        <d>Y</d>
        <e>Z</e>
    </c>
</a>
위와 같을 때 a/b/:X, a/c/d:Y text정보는 자식노드로 생각할 수 있다.
attribute는 여러 값을 가질 수 있음, b노드에서 w=5, x=1, t=10 이런식으로.
'''

# example 1
# import built-in funciton
import xml.etree.ElementTree as ET
data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +10 3444 6916
    </phone>
    <email hide="yes"/>
</person>
'''
tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
# email tag에 hide attribute의 값, attribute는 여러개 있을 수 있기 때문에 찾을 값을 명시 해야함
print('Attr:',tree.find('email').get('hide'))


# example 2
input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user') # users/user tag를 갖는 object 2개 list로 반환
print('User count: ' , len(lst))
for item in lst:
    print('id: ', item.find('id').text)
    print('name: ', item.find('name').text)
    print('attr ', item.get('x')) # list 속에서 user가 가장 상위 attribute는 tag없음
