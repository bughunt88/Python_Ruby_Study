#파이썬 오버라이드 형식
class C1:
    def m(self):
        return 'parent'

#비어있는 클래스 사용하려면 pass가 필요함
class C2(C1):
    #부모의 있는 m()메소드를 오버라이드 해서 child 출력하게 바꿈
    def m(self):
        #super()는 부모 클래스의 메소드를 불러낸다
        return  super().m() + ' child'
    pass

o = C2()
print(o.m())
