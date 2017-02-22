#파이썬 객체 연습

#객체의 이름은 대소문자 상관 없다
class Cal(object):
    #파이썬에 매개변수를 만들려면 self를 써줘야 원하는 순서로 만들어진다 (self 없으면 반대로 적용)

    #__init__은 파이썬의 생성자
    def __init__(self, v1, v2):

        #이안에서 v1,v2는 지역변수
        print(v1, v2)
        #파이썬의 매소드들은 첫번째 매개변수를 꼭 지정해줘야한다, 첫 매개변수가 인스턴스 변수이다
        self.v1 = v1
        self.v2 = v2
        #인스턴스 변수 self는 다른이름으로 쓸 수 있지만 관습적으로 self라고 사용한다
    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2

c1 = Cal(10,10)
print(c1.add())
print(c1.subtract())

c2 = Cal(30,20)
print(c2.add())
print(c2.subtract())
