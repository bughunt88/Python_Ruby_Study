# 파이썬 input 연습 2

in_str = input("아이디 입력하세요")
#input으로 숫자가 들어오면 string으로 받기 때문에 아래 변수도 string으로 해줘야 한다 "" 필요!
real_kk = "11"
real_bb = "bb"


if real_kk  == in_str:
  print("hello!, bughunt")
elif real_bb == in_str:
    print("hello!, bughunt!!!!")
else:
  print("who are you?")
