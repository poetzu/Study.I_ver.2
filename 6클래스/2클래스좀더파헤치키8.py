
#주제 : getter메소드  setter메소드

# 2클래스좀더파헤치기7.py파일의 소스코드를 이용해
# 원둘레를 변경하고 싶다면 어떻게 해야 할까요?
#클래스 외부에서 직접 __radius속성에 접근 할수 없기 떄문에
#간접적으로 접근할 수 있는 방법을 찾아야 합니다
#getter와 setter메소드는 프라이빗으로 선언된 변수의 값으 추출하거나
#변경할 목적으로 간접적으로 속성에 접근하도록 해주는 메소드 이다.

#예제 . getter setter메소드 사용한 예제

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

    #겟터 셋터 메소드 선언
    def get_radius(self):
        return self.__radius

    def set_radius(self, value):
        #__radius인스턴스 변수에 저장할 값을 양의 숫자로만 한정하게 하기
        if value <= 0:
            raise TypeError("길이는 양의 숫자여야 합니다")
        self.__radius = value


#----------------------------------------------------------------------------------
#원의 둘레와 넓이를 구합니다
circle = Circle(10)
print("# 원의 둘레와 넓이를 구합니다")
print("원의 둘레 :", circle.get_circumference()   )
print("원의 넓이 :", circle.get_area())

print()

#클래스외부에서 __radius프라이빗 인스턴스 변수에 접근 해보자
print("# __radius 프라이빗 인스턴스 변수의 값 ")
# print(circle.__radius)
print(circle.get_radius())


circle.set_radius(2)
print("# 원의 둘레와 넓이를 구합니다")
print("원의 둘레 :", circle.get_circumference())
print("원의 넓이 :", circle.get_area())

