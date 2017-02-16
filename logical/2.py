# 파이썬 중첩 if 연습

input_id = input("아이디 입력하세요\n")
#input으로 숫자가 들어오면 string으로 받기 때문에 아래 변수도 string으로 해줘야 한다 "" 필요!
real_id = "bughunt"

input_pw = input("비밀번호를 입력해주세요\n")
real_pw = "11"

if real_id == input_id:

    if real_pw == input_pw:
        print("hello!")
    else:
        print("잘못된 비밀번호입니다.")

else:
  print("잘못된 아이디 입니다.")
