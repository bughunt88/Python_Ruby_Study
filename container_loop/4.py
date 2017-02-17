# 파이썬 배운것 연습
input_id = input("아이디 입력하세요")

members = ['bughunt', 'hs2207']

for member in members:
    if member==input_id:
        print('hello!, '+ member)

        #프로그램을 끝나게 하는 코딩
        import sys
        sys.exit()
        
print("who are you?")


# #input으로 숫자가 들어오면 string으로 받기 때문에 아래 변수도 string으로 해줘야 한다 "" 필요!
# real_kk = "bughunt"
# real_bb = "hs2207"
#
#
# if real_kk  == in_str:
#   print("hello!, bughunt")
# elif real_bb == in_str:
#     print("hello!, hs2207")
# else:
#   print("who are you?")
