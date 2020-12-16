
#주제 :  객체(인스턴스)가  어떤 클래스로 부터 만들어 졌는지 확인할수 있도록하는 isinstance()함수

#문법
# isinstance(인스턴스,클래스)
#설명 : 함수의 첫번째 매개변수에 객체(인스턴스), 두번째 매개변수에는 클래스를 입력합니다
# 이때 인스턴스가 해당 클래스를 기반으로 만들어 졌다면  True,
# 전혀 상관이 없는 인스턴스와 클래스 관계라면  False를 리턴 함.

#학생 클래스 선언
class Student:
    def study(self):
        print("공부를 합니다.")

#선생님 클래스 선언
class Teacher:
    def teach(self):
        print("학생을 가리킵니다")

#교실 내부의 객체 리스트를 생성 합니다
classroom = [Student(), Student(), Teacher(), Student(), Student() ]

#반복을 적용해서 적절한 함수를 호출하게 합니다
for person in classroom: #[Student(), Student(), Teacher(), Student(), Student() ]
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()

#설명 : Student와 Teacher클래스를 생성하고,
# classroom이라는 리스트 내부에 객체들을  넣습니다.
# 그리고 for반복을 적용 했을떄, 요소가  Student클래스의 인스턴스인지,....
# Teacher클래스의 인스턴스인지 확인하고  각각의 대상이 가지고 있는 적절한 함수를 호출합니다.


