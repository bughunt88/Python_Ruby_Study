#루비 배열과 블록 2
arr=[1,3,56,7,14,42]


#한줄이면 {}를 사용하는 것을 권장함
arr.delete_if() { |item|
  item > 7
}
puts arr


#여러줄이면 do, end를 사용하는 것을 권장함
arr.delete_if() do |item|
  item > 7

end
puts arr
