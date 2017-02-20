# 루비 배운것 연습
puts('아이디를 입력하세요')
input_id = gets.chomp()

members = ['bughunt', 'hs2207']

  for member in members do
    if member == input_id
      puts("hello!, " + member)
      exit
    end

  end
puts('who are you?')
