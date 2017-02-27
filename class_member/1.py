#파이썬 클래스 메소드
class Cs:

    #def 뒤에 메소드 명은 아무거나 써도 상관없다
    #대신 @뒤에는 정확하게 명시해야한다
    @staticmethod
    def static_method():
        print("static_method")
    @classmethod
    def class_method(cls):
        print("class_method")
    def instance_method(self):
        print("instance_method")

i = Cs()
Cs.static_method()
Cs.class_method()
i.instance_method()
