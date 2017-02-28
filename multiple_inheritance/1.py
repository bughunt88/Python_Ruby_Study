#파이썬 다중상족의 형식

class c1():
    def c1_m(self):
        print("c1_m")

class c2():
    def c2_m(self):
        print("c2_m")

class c3(c1, c2):
    pass

c = c3()

c.c1_m()
c.c2_m()
