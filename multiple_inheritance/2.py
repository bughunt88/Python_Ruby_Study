#파이썬 다중상족의 단점
#다중상속 하는 중 메소드가 안겹치면 좋지만 겹치게 된다면 우선순위에 의해 실행됨 그래서 문제가 발생

class C1():
    def c1_m(self):
        print("c1_m")
    def m(self):
        print("C1 m")

class C2():
    def c2_m(self):
        print("c2_m")
    def m(self):
        print("C2 m")

class C3(C2, C1):
    def m(self):
        print("C3 m")

c = C3()
c.c1_m()
c.c2_m()
c.m()
