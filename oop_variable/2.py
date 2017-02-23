#파이썬 get, set 메소드
class C :
    def __init__(self, x):
        self.value = x
        
    def getValue(self):
        return self.value
    def setValue(self, v):
        self.value = v

c1 = C(10)
print (c1.getValue())
c1.setValue(20)
print (c1.getValue())
