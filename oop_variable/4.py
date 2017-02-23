#파이썬 인스턴스 외부에 사용 못하게 하는 법
class C :
    def __init__(self, x):
        self.__value = x

    def show(self) :
        print(self.__value)

c1 = C(10)

#__ 쓰면 아래는 불가능
#print (c1.__value)

#메소드 안에서 인스턴스 변수 접근은 가능하다
c1.show()
