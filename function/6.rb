#루비의 함수에서 일어나는 생략
def f1()
  return 'f1'
end
puts(f1())

#루비에서는 ()를 생략 할 수 있다.
def f2
  return 'f2'
end
puts(f2())

def f3
  return 'f3'
end
puts(f3)

def f4(a1)
  return a1
end
puts(f4('f4'))

#()생략했을때 띄어쓰기로 사용 할 수 있다
def f5 a1
  return a1
end
puts(f5 'f5')
#내장함수도 () 생략 가능!
puts f5 'f5'

def f6
  return 'f6'
end
puts f6

#return을 생각해도 자동으로 값을 넣어준다
def f7
  'f7'
end
puts f7

def f8
  a=1
  b=2
  a+b
end
puts f8
