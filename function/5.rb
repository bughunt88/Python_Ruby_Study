# 루비 함수 연습
puts('아이디를 입력하세요')
input_id = gets.chomp()

def login(_id)
  members = ['bughunt', 'hs2207']
    for member in members do
      if member == _id
        return true
      end
    end
    return false
end

if login(input_id)
  puts('hello ',+input_id)
else
  puts('who are you?')
end


# members = ['bughunt', 'hs2207']
#
#   for member in members do
#     if member == input_id
#       puts("hello!, " + member)
#       exit
#     end
#
#   end
# puts('who are you?')
