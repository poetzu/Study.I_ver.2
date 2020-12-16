
#주제  : 프라이빗 변수
#파이선은 클래스 내부의 변수를 ???? 클래스 외부에서 사용하는 것을 막고 싶을때
#  인스턴스변수이름을?   __변수명 형태로 선언 합니다

# math라는 이름의 모듈을 불러옵니다
import math

#클래스 선언
class Circle:

    def __init__(self, radius): #생성자
        self.__radius = radius  # 인스턴스변수  ->   __변수명 으로 선언후 값을 저장함

    def get_circumference(self): #메소드
        return 2 * math.pi  * self.__radius  # 인스턴스변수에 저장된 값을 사용함

    def get_area(self):#메소드
        return math.pi * (self.__radius ** 2) #인스턴스변수에 저장된 값을 사용함
#----------------------------------------------------------------------------------
#원의 둘레와 넓이를 구합니다
circle = Circle(10)
print("# 원의 둘레와 넓이를 구합니다")
print("원의 둘레 :", circle.get_circumference()   )
print("원의 넓이 :", circle.get_area())

print()

#클래스외부에서 __radius프라이빗 인스턴스 변수에 접근 해보자
print("# __radius 프라이빗 인스턴스 변수의 값 ")
print(circle.__radius)

#결론 : 클래스 내부에서 __radius를 사용하는 것은 아무 문제 없지만,
#   클래스 외부에서  __radius를 사용하려 할때 그런 속성은 없다는 오류를 출력합니다



