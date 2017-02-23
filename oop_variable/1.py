#파이썬 인스턴스 변수
class C :
    def __init__(self, x):
        self.value = x
#인스턴스 메소드 안에서 인스턴스 변수에 접근하는것이 가능하다
    def show(self):
        print((self.value))

c1 = C(10)
print (c1.value)
c1.value=20
print (c1.value)
c1.show()
