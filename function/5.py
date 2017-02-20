# 파이썬 배운것 연습
input_id = input("아이디 입력하세요")

def login(_id):
    members = ['bughunt', 'hs2207']
    for member in members:
        if member==_id:
            return True
    return False

if login(input_id):
    print('hello ' + input_id)
else:
    print('who are you?')
