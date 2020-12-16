
#주제 : 클래스 내부에 선언할 수 있는 파이썬에서 제공해주는 매직 메소드
#매직 메소드는 메소드이름 앞과 뒤에 언더스코어(__) 두개가 연속으로 붙어 있는 메소드를 말합니다
# 예)  __메소드이름__()

#예제1.    __add__() 메소드는  +연산자 역할을 한다.
class coordinate:
    #생성자
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #더하기 + 연산자 역할을 하는 메소드
        # self는  coord1, other변수에는 coord2가 들어가서
        # self와 other로 지칭한 두개의 숫자 묶음을 x는 x끼리 , y는 y끼리 더하기를 해서
        # coordinate클래스의  객체 형태로 반환하도록 한다는 뜻입니다.
    def __add__(self, other):
        return coordinate(self.x + other.x, self.y + other.y)
#------------------------------------------------------------------------
coord1 = coordinate(5, 7)

coord2 = coordinate(3, 9)
#두 객체를 더하여  저장
coord3= coord1 + coord2 #풀어서 쓰면 coord1.__add__(coodr2)
print(coord3.x) # 8
print(coord3.y) # 16

# __add__() 외에도 다음과 같은 연산자들이 매직 메소드로 사용됩니다
#
# __sub__()    -
# __mul__()    *
# __lt__()    <
# __le__()    <=
# __eq__()    ==
# __ne__()    !=
# __gt__()    >
# __ge__()    >=
#==============================================================
                #Student("홍길동",50,40,100,40).get_average()
#예제2.
class Student:
    #생성자
    def __init__(self, name, korean, math, english, science):
        #인스턴스변수를 새로이 만들어서 매개변수값을 얻어 저장
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    #메소드  합
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    #메소드  평균
    def get_average(self):
        return self.get_sum() / 4

    #매개변수로 전달 받는 객체를 문자열 정보로 만들어서 반환 해주는 메소드
    def __str__(self, student):
        return "{}\t{}\t{}".format(self.name,
                                   self.get_sum(student),
                                   self.get_average(student))
    def __eq__(self, value):  #매개변수로 전달 받는 객체들의 점수의 총합이 같냐? 묻는 메소드
        return self.get_sum() == value.get_sum()

    def __ne__(self, value): # 매개변수로 전달받는 객체들의 점수의 총합이 다르냐? 묻는 메소드
        return self.get_sum() != value.get_sum()

    def __gt__(self, value):
        return self.get_sum() > value.get_sum()

    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()

    def __lt__(self, value):
        return self.get_sum() < value.get_sum()

    def __le__(self, value):
        return self.get_sum() <= value.get_sum()

#--------------------------------------------------------------------

# 학생 인스턴스들을 생성하여 리스트에 저장
student = [
    Student("윤인성", 87,98,88,95),
    Student("연하진", 92,98,96,98),
    Student("구지연", 76,96,94,90),
    Student("나선주", 98,92,96,92),
    Student("윤아린", 95,98,98,98),
    Student("윤명월", 64,88,92,92)
]

#학생 인스턴스 따로 생성
student_a  = Student("윤인성", 87, 98, 88, 95)
student_b  = Student("연하진", 92, 98, 96, 98)

print(student_a == student_b)    # 풀어서 쓰면  student_a.__eq__(student_b)

print(student_a != student_b)    # 풀어서 쓰면 student_a.__ne__(student_b)

print(student_a > student_b)     #풀어서 쓰면 student_a.__gt__(student_b)

print(student_a >= student_b)    #풀어서 쓰면 student_a.__ge__(student_b)

print(student_a < student_b)    #풀어서 쓰면  student_a.__lt__(student_b)

print(student_a <= student_b)  # 풀어서 쓰면 student_a.__le__(student_b)



