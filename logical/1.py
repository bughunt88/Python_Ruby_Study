# 파이썬 or 연습

in_str = input("아이디 입력하세요\n")
#input으로 숫자가 들어오면 string으로 받기 때문에 아래 변수도 string으로 해줘야 한다 "" 필요!
real_kk = "bughunt"
real_bb = "admin"


if real_kk == in_str or real_bb == in_str:
  print("hello!")

else:
  print("who are you?")
