#루비의 배열과 블록

#each는 원소를 하나씩 꺼내는 일을 함
['A','B','C'].each(){|i| puts i.downcase()}


#위와 아래 코드는 같은 내용이다

arr=['A','B','C']

for value in arr
  puts value
end
