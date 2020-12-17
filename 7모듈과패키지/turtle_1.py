

# 거북이 그래픽(Turtle Graphic)모듈은
# 1960년대 logo라는 프로그래밍 언어의 일부로 개발된 컴퓨터 그래픽 방식의 모듈이다
# 꼬리에 잉크가 묻은 거북이를 종이에 올려 놓고 리모컨 조작하듯 듯한 방식으로 동작합니다

# 거북이 그래픽 모듈은 파이썬의 기본모듈이므로 파이썬만 설치하면 바로 사용할수 있습니다
import turtle as t

#파이썬은  거북이 그래픽 모듈을 시작하면  창(window)을 적당한 크기로 만듭니다
#그런 다음 배경을 하얗게 칠하고  창의 한가운데인 좌표값(0,0)에 거북이를 오른쪽으로 향하도록 세워 놓고
#(x 축의  + 방향), 사용자가 명령을 내리기를 기다립니다

#거북이 모양을 따로 지정하지 않으면  기본으로 화살촉 모양이 표시 됩니다.
#기본으로 화살촉 모양을 표시하려면  t.shape("classic")
#거북이 모양을 표시 하려면 t.shape("turtle")
#세모 모양을 표시 하려면 t.shape("triangle")
t.shape("classic")

#삼각형 그리기
t.forward(100) # 거북이 모양을 100만큼 앞으로 이동시키기
t.left(120) # 거북이 모양을 왼쪽으로 120도 회전합니다

t.forward(100) # 거북이 모양을 100만큼 앞으로 이동시키기
t.left(120) # 거북이 모양을 왼쪽으로 120도 회전합니다

t.forward(100) # 거북이 모양을 100만큼 앞으로 이동시키기
t.left(120) # 거북이 모양을 왼쪽으로 120도 회전합니다

#사각형 그리기
t.forward(100) #거북이 100만큼 앞으로 이동
t.left(90) # 거북이 왼쪽으로 90도 회전 시킵니다

t.forward(100) #거북이 100만큼 앞으로 이동
t.left(90) # 거북이 왼쪽으로 90도 회전 시킵니다ㅍ

t.forward(100) #거북이 100만큼 앞으로 이동
t.left(90) # 거북이 왼쪽으로 90도 회전 시킵니다

t.forward(100) #거북이 100만큼 앞으로 이동
t.left(90) # 거북이 왼쪽으로 90도 회전 시킵니다

#원그리기
#반지름이 50인 원을 그린다
t.circle(50)

