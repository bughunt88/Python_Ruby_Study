#파이썬 모듈 연습

#bughunt 파일에 a함수만 가져온다, as는 함수 명을 변경시킨다
from bughunt import a as z

#hs2207 파일 모든것을 가져온다, as는 파일명을 변경시킨다
import hs2207 as k


#from으로 가져왔다면 함수명만 쓴다
print(z())

#import로 가져왔다면 모듈명.함수명으로 쓴다, as를 쓴다면 as명.함수명
print(k.a())
