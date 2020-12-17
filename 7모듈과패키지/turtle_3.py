# 반복 기능으로 도형을 그리는 프로그램



# 거북이 모듈 turtle 불러오기
import  turtle as t

#삼각형 그리기  for문이용
for x in range(3): #[0,1,2] #세번 반복
    #거북이 모양을 100만큼 앞으로 이동시킵니다
    t.forward(100)
    #거북이 모양을 왼쪽으로 120도 회전 시킵니다
    t.left(120)


#사각형 그리기 for문이용
for x in range(4):
    t.forward(100)
    t.left(90)

#원그리기 (반지름 50)
t.circle(50)