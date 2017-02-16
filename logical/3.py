# 파이썬 and 연습

input_id = input("아이디 입력하세요\n")
input_pw = input("비밀번호를 입력해주세요\n")
#input으로 숫자가 들어오면 string으로 받기 때문에 아래 변수도 string으로 해줘야 한다 "" 필요!
real_id = "bughunt"
real_pw = "11"

if real_id == input_id and real_pw == input_pw:
    print("hello!")
else:
  print("로그인에 실패했습니다..")

  #파이썬은 들여쓰기에 민감하다 잘 처리하자
