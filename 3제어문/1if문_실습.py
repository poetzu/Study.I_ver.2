# if문이란?
# 프로그래밍에서 조건을 판단하여 해당 조건에 맞는 상황을 수행하는데 사용하는 제어문

#if문의 기본 구조
    # if 조건문:
    #   수행할 문장1
    #   수행할 문장2
    #   .......
    # else:
    #   수행할 문장A
    #   수행할 문장B

#예제1.
money = True

if money:
    print("택시를")
#print("타고")     #들여 쓰기 하지 않아 에러 발생
    print("가라")

#결론 :
#       -들여쓰기는 언제나 같은 너비로 해야 한다.
#       -들여쓰기는 스페이스바 4번을 사용하는 것을 권장함.

#조건문에 비교 연산자를 사용하는 방법
#예제2.
x = 3
y = 2
print(x > y)  # True
print(x < y)  # False
print(x == y) # False
print(x != y) # True

#예제3. 조건식 :  만약 3000원 이상의 돈을 가지고 있으면 택시를 타고  그렇지 않으면 걸어가라!  if문 작성
money = 2000  # 2000원을 가지고 있다
if money >= 3000:
    print("택시를 타고 가라")  #문장이 실행 되지 않는다
else:
    print("걸어 가라") #문장이 실행됨

#   연산자     설명
#   x or y      x와 y둘 중에 하나만 참이면 참이다
#   x and y     x와 y 모두 참이어야 참이다
#   not x       x가 거짓이면 참이다

# 조건문에 and, or, not 연산자를 쓰는 방법
#예제4. 돈이 3000원 이상 있거나  카드가 있다면 택시를 타고  그렇지 않으면 걸어가라.  if문으로 작성
money = 2000
card = True
if money >= 3000  or card:  #money는 2000이지만  card가 True이기때문에 조건문의 결과가 참이다.
    print("택시를 타고 가라") #출력됨
else:
    print("걸어 가라") #출력되지 않음

# in    ->   ~안에 있는가?
# not in ->  ~안에 없는가?
#예제5.   1이  [1,2,3]리스트 안에 있는가? 라는 물음에 참이므로 True를 반환함
print(1 in [1,2,3] )

#예제6.  1이  [1,2,3]리스트 안에 없는가? 라는 물음에 거짓이므로  False를 반환함
print(1 not in [1,2,3])

#예제7. 튜플에  in 적용한 예제
# 'a' 가  ('a','b','c')튜플 안에 있는가? 라는 물음에 참이므로 True를 반환함
print( 'a' in  ('a','b','c') )

#예제8. 문자열에 not in 적용한 예제
# 'j' 가  'python'문자열안에 없는가?라는 물음에  참이므로 True를 반환함
print( 'j' not in 'python')

#예제9. 만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가라   in을 적용 해보자.
porket = ['paper','cellphone','money']  # 주머니(리스트)내부에  종이, 휴대전화, 돈이 있다.

if 'money' in porket:  # 주머니에  돈이 들어 있는가?  True를 반환함
    print("택시를 타고 가라.")
else:
    print("걸어 가라.")

#다양한 조건을 판단하는 elif문
#예제10. 아래의 조건들을 이용하여 if elif else로 작성 하시오.
# 주머니에 돈이 있으면 "택시를 타고가라"
# 주머니에 돈이 없고  카드가 있으면  "택시를 타고가라"
# 주머니에 돈도 없고  카드도 없으면 "걸어가라"

# 주머니에 종이, 휴대전화를 저장
porket = ['paper','cellphone']
card = True  #카드 있음
#주머니에 돈이 있으면  택시를 타고가라
if 'money' in porket:
    print("택시를 타고 가라.")
elif card: #주머니에 돈이 없고 카드가 있으면
    print("택시를 타고 가라.")
else:#주머니에 돈도 없고 카드도 없으면
    print("걸어 가라")

#예제11.
score = 70

if score >= 60:
    message = "success"
else:
    message = "failure"

print(message)

#파이썬의 조건부 표현식을 사용하면 위의 코드를 간단히 표현 할수 있다.
#조건부 표현식 사용
message = "success" if score >= 60 else "failure"
print(message)

#참고 : 조건부 표현식 문법
# 조건문이 참인 경우사용할 값   if  조건문  else 조건문이 거짓일 경우 사용할 값






























