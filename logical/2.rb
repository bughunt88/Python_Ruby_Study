# 루비 중첩 if 연습



puts('아이디를 입력하세요')
in_id = gets.chomp()
puts('비밀번호를 입력해주세요')
in_pw = gets.chop()
#gets.chomp으로 숫자가 들어오면 string으로 받기 때문에 아래 변수도 string으로 해줘야 한다 "" 필요!
real_id = "bughunt"
real_pw = "11"


if real_id   == in_id

  if real_pw  == in_pw
    puts("hello!")
  else
    puts('잘못된 비밀번호 입니다.')
  end

  else
  puts("잘못된 아이디 입니다.")
end
