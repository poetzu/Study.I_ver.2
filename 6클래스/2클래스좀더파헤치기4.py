
#주제 : 클래스 변수와 메소드
#인스턴스가 속성과 기능을 가질수도 있지만,
#클래스가 속성(변수)과 기능(함수)을 가질수도 있습니다.

#1. 클래스 변수 만들기
#클래스 변수는 class구문 바로 아래의 단계에 변수를 선언하기만 하면 됩니다.

    # class 클래스이름:
    #   클래스변수 = 값

#2. 클래스 변수에 접근하기

    # 클래스이름.변수이름

#예제      Student("윤인성", 87,98,88,95)
class Student:
    #클래스 변수 선언
    count = 0
    #생성자
    def __init__(self, name, korean, math, english, science):
        #인스턴스 변수 선언 후 초기화
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        #클래스 변수에 접근하여  값을 설정
        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count)     )


#학생 인스턴스들을 생성하여 리스트 공간에 저장
student = [
    Student("윤인성", 87,98,88,95),
    Student("연하진", 92,98,96,98),
    Student("구지연", 76,96,94,90),
    Student("나선주", 98,92,96,92),
    Student("윤아린", 95,98,98,98),
    Student("윤명월", 64,88,92,92)
]

#출력합니다
print()
print("현재 생성된 총 학생 수는 {}명 입니다.".format(Student.count))
#Student클래스 외부에서도 클래스변수에 접근 하여  클래스 변수값을 얻어 사용할때...
#클래스이름.클래스변수이름








