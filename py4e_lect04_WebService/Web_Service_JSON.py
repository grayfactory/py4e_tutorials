'''
JSON represents data as nested 'list' and 'dictionaries'
: json 객체를 바로 python dictionarie로 읽기 때문에
: find, get, findall 을 사용할 필요가 없다.
'''

import json
# example 1
data = '''{
"name" : "gray",
"phone" : {
    "type" : "intl",
    "number" : "+01 3344 2229"
    },
"email" : {
    "hide" : "yes"
    }
}
'''
info = json.loads(data)
print('Name: ', info['name']) # dict으로 읽기 때문에 표문문법 사용가능
print('hide: ', info['email']['hide'])

# example 2
input = '''[
    { "id" : "001",
      "x" : "2",
      "name" : "gray"
    },
    { "id" : "002",
      "x" : "7",
      "name" : "park"
    }
]
'''
# dict을 2개 가진 list
info = json.loads(input)
print('user count: ' , len(info))
for user in info:
    # print(f'Name: {user['name']} \nID: {user['id']} \n Arribute: {user['x']}')
    name = user['name']
    id = user['id']
    attr = user['x']
    print(f'Name: {name} \nID: {id} \nArribute: {attr}')
