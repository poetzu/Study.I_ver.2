
#while문이란?
#반복해서 문장을 수행해야 할 경우 while반복문을 사용한다.

#while문의 기본구조
    # while 조건문:
    #       수행할 문장1
    #       수행할 문장2
    #       수행할 문장3
    #       ....
#설명 : while문은 조건문이 참인 동안에 while문 아래의 문장이 반복해서 수행된다.

#예제1. "열번 찍어 안넘어가는 나무 없다"는 속담을 while반복문으로 만들자

#나무를 찍은 횟수 저장할 변수
treeHit = 0

#나무를 찍은 횟수가 10보다 작은 동안 반복
while treeHit < 10:
    #나무를 찍은 횟수 1증가
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." %treeHit)
    #만약 나무를 열번 찍으면?
    if treeHit == 10:
        print("나무 넘어 갑니다.")

#예제2. While반복문을 강제로 빠져 나가게 하는 break문
coffee = 10  #자판기에 커피가 10개 있다.
money = 300  #자판기에 넣을 돈은 300원이다.

while money: #money가 300으로 고정 되어 있기 떄문에 money는 0이 아니기 떄문에 항상 참이다.
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1  #while문을 한번 돌때 coffee의 개수가 1개씩 줄어 든다.
    print("남은 커피의 양은 %d개 입니다."  %coffee)
    #coffee변수에 저장된 커피의 개수가 0이 되면 (자판기에 커피가 모두 소모 되었다면)
    if coffee == 0:
        print("커피가 다 떨어 졌습니다. 판매를 중지합니다.")
        break #break문이 호출되어 while반복을 빠져 나간다

#예제3. while반복문과 break문 사용 -> 키보드로 부터 입력 받는 예제
coffee = 10 #자판기에 커피가 10개 있다

# while True: #무한 반복
#     money = int(input("돈을 넣어주세요:"))
#     if money == 300: #자판기에 300원을 넣었다면
#         print("커피를 줍니다.")
#         coffee = coffee - 1 #커피를 줬으니 커피 하나 차감
#     elif money > 300:#자판기에 300원이상을 넣었다면
#         print("거스름돈 %d를 주고 커피를 줍니다." %(money-300))
#         coffee = coffee - 1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개입니다." %coffee)
#
#     if coffee == 0:
#        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#        break

#예제4. while반복문과  continue문 사용
# 1부터 10까지의 숫자 중에서  홀수만 반복해서 출력 하는 예제
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue # a변수의 값을 2로 나눈 나머지값이 0이면 (짝수)이면
                 # continue문을 만나  while반복문의 조건식으로 가서 조건을 다시 판단 한다.
    print(a)
































