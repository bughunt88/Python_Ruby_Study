#루비 컨테이너 심화
al = ['a', 'b', 'c' , 'd']

#.length은 원소 갯수 알려주는 것
puts(al.length)

#루비에서 .push는 배열에 원소 추가하는것
al.push('e')
print(al)

#루비에서 .delete_at()는 배열에 원소 삭제하는것
al.delete_at(0)
print("\n")
print(al)
