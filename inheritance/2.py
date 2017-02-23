#파이썬 상속 응용

class Cal(object):
    #생성자
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2

    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2

    #set,get 메소드
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1

#cal 클래스를 상속받음
class CalMultiply(Cal):
    def multiply(self):
        return self.v1*self.v2

c1 = CalMultiply(10,10)
print(c1.add())
print(c1.multiply())


#상속에 상속도 가능하다
class CalDivide(CalMultiply):
     def divide(self):
         return self.v1/self.v2

c2 = CalDivide(10,10)

#프린트에 클래스 명 쓰면 어느클래스에서 나온 결과인지 볼 수 있다
print(c2, c2.add())
print(c2, c2.multiply())
print(c2, c2.divide())
