

# 마음대로 걷는 거북이 프로그램 만들기
import turtle as t
import  random

#거북이 모양의 그래픽을 사용하자
t.shape("turtle")
t.speed(0)

#거북이 모양의 아이콘을 500번 반복해서 움직여서 그림을 그리자
for x in range(500):
    # 1~ 360 사이의 임의의수 아무수나 골라 a변수에 저장
    a = random.randint(1, 360)
    # a변수에 저장된 각도로  거북이의 방향을 돌립니다
    t.setheading(a)
    # 거북이를 10만큼 앞으로 이동 시켜 선 긋기
    t.forward(10)




