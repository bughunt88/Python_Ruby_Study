# 루비 or 연습



puts('아이디를 입력하세요')
in_str = gets.chomp()
#gets.chomp으로 숫자가 들어오면 string으로 받기 때문에 아래 변수도 string으로 해줘야 한다 "" 필요!
real_kk = "bughunt"
real_bb = "adin"


if real_kk  == in_str or real_bb == in_str
  puts("hello!")
  else
  puts("who are you?")
end
