#루비 컨테이너 연습


#배열은 루비에서 Array라고 한다 ([]와 ,를 사용해서 구분한다)
names = ['bughunt', 'hs2207', 'kkk']
# .class는 파일 타입을 알 수 있게 해주는 코딩
puts(names.class)

#배열에서 하나의 원소를 출력하고자 하면 변수명[index]로 출력 할 수 있다
puts(names[0])

#원소 값을 변경 할 수 있다.
names[0] = 'bughunt88'
print(names)

#전반적으로 파이썬과 똑같다
