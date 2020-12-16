
#클래스 내부에 존재하는 생성자란?
#클래스 이름과 같은 함수를 생성자라고 부릅니다
#클래스 내부에  __init__라는 함수를 만들면 객체를 생성할때 처리할 내용을 작성할수 있다.
    #문법
    #class 클래스이름:
    #   def __init__(self, 추가적인 매개변수):
    #       코드작성

#메소드란?
#클래스가 가지고 있는 함수를 메소드라고 부릅니다.
    #문법
    #class 클래스이름:
    #   def 메소드이름(self,추가적인 매개변수):
    #       코드작성

#예제1. 인스턴스가 생성될때 자동으로 호출되어
#      변수를 초기화 해주는 __init__생성자 및 메소드 선언하여 클래스 만들기
class Dog: #클래스 선언

    #__init__변수 초기화 메소드 (생성자) 선언
    #설명 : 매개변수 self에는  Dog클래스로 부터 생성한 자기자신의 Dog객체를 전달받아 사용 한다.
    #self.name구문은  Dog객체에 객체변수 name이 새롭게 생성되고,
    #self.name = name구문 중에서.. name은  (self,name)구문중 매개변수 name으로부터 전달받은 값을
    #Dog객체의 객체변수name에 저장하는 구문이다.
    def __init__(self,name):
        self.name = name

    #bark(self)메소드 선언
    #설명 : 매개변수 self에는 클래스 자신의 객체인 Dog객체를 전달 받는다
    #print()구문은 생성한 Dog객체의 객체변수 name에 저장된 값을 참조하여 출력하고 있다.
    def bark(self):
        print(self.name + "가 멍멍하고 짖는다.")

my_dog = Dog("삼식이") # 인스턴스 생성(객체 생성)시 매개변수가 하나인 생성자를 호출하여
                      # name변수값을 초기화함
my_dog.bark() #인스턴스의 메소드 호출


#예제2. 클래스 내부에 생성자, 메소드 선언하기
class Student:

    #생성자
    def __init__(self,name,korean,math,english,science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    #메소드  :  점수 합구하기
    #참고 :  \ 줄바꿈을 하지 않고 계속해서 그줄에 이어 나간다는 뜻
    def get_sum(self):
        return self.korean + self.math + \
               self.english + self.science

    #메소드 : 평균구하기
    def get_average(self):
        return self.get_sum() / 4

    #메소드
    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())
#------------------------------------------------------------------------

#Student인스턴스를 생성하여 리스트에 저장
students = [
    Student("윤인성", 87, 98, 88, 95), #인스턴스 생성(객체생성)
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

#학생 한명의 정보씩 반복하여 출력
print("이름", "총점", "평균", sep="\t")
for student in students:
    #출력합니다
    print(student.to_string())


#예제3. 클래스 변수와 인스턴스 변수
#- 클래스에서도 변수가 선언된 위치에 따라 변수의 유효범위가 달라지며,
#  이에 따라 다음과 같이 구분 할수 있습니다
    #1. 클래스 변수
    #  - 해당 클래스에서 생성된 모든 인스턴스가 값을 공유하는 변수
    #2. 인스턴스 변수
    # -   __init__ 생성자 내에서 선언된 변수로
    #     인스턴스가 생성될때 마다 새로운값이 할당되는 변수 입니다.

class Dog:
    #클래스 변수 선언
    sound = "멍멍"

    #생성자 선언
    def __init__(self,name):
        #인스턴스 변수 선언
        self.name = name

    #일반 메소드 선언
    def bark(self):
        print(self.name + "가 멍멍하고 짖느다.")

#인스턴스 생성
my_dog = Dog("삼식이")
your_dog = Dog("콩이")

#클래스 변수에 접근
print(my_dog.sound)
#인스턴스 변수에 접근
print(my_dog.name)

#클래스 변수에 접근
print(your_dog.sound)
#인스턴스 변수에 접근
print(your_dog.name)










