#파이썬 다중상속의 활용

#cal 클래스를 상속받음
class CalMultiply():
    def multiply(self):
        return self.v1*self.v2

#상속에 상속도 가능하다
class CalDivide():
     def divide(self):
         return self.v1/self.v2

class Cal(CalMultiply, CalDivide):
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

c = Cal(100, 10)
print(c.add())
print(c.multiply())
print(c.divide())
