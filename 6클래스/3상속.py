#상속이란?
# - 새로운 클래스를 만들때  기존에 만들 었던  클래스의 기능을 그대로 상속하면서
#   새로운 기능을 추가하는 것을 말함
#   이때 기존에 만들 었던 클래스를 부모클래스 또는 기초클래스라고 부르며,
#    상속을 통해서 새롭게 생성되는 클래스를 자식 클래스 또는 파생 클래스라고 부릅니다
#--------------------------------------------------------------------------------
#클래스 상속 하기 문법
    # class 자식클래스명(부모클래스명):

    #설명 : 파이선에서 클래스를 선언할떄 다른 클래스를 상속받고 싶다면?
    # 소괄호()를 사용하여 그안에 상속받고 싶은 클래스명을 넣어 전달함으로써
    # 해당 클래스의 모든 멤버를 상속받을수 있습니다

#예제
class Bird:  # 부모클래스

    def __init__(self):
        self.flying = True

    def birdsong(self):
        print("새소리")

class Sparrow(Bird): # Sparrow클래스가 Bird클래스를 상속받아 선언됨

    def birdsong(self):
        print("짹짹")

#---------------------------------------------------------------------------------
my_pet = Sparrow()

#이때  Sparrow클래스는  Bird클래스를 상속받았기 때문에 , Sparrow클래스에서 선언하지 않았지만
# 부모클래스인 Bird클래스에 존재하는 flying속성값이 True를 자유롭게 사용할수 있는 것입니다.
print(my_pet.flying) #True

my_pet.birdsong() #짹짹
#---------------------------------------------------------------------------------
#메소드 오버라이딩이란?
# - 상속관계에 있는 부모클래스에서 이미 정의된 메소드를 자식클래스에서 같은 이름으로 사용하되
#   메소드의 구현부만 재정의 해서 사용 하는 것을 메소드오버라이딩이라고 합니다

#예제
class Bird:  # 부모클래스

    def __init__(self):
        self.flying = True

    def birdsong(self):
        print("새소리")

class Sparrow(Bird): # Sparrow클래스가 Bird클래스를 상속받아 선언됨

    def birdsong(self): # Bird클래스의 메소드를 재정의 했음 (오버라이딩 했음)
        print("짹짹")

#클래스 선언시 Bird클래스의 모든 멤버를 상속 받는다.
class Chicken(Bird):
    #생성자
    def __init__(self):
        self.flying = False
#--------------------------------------

my_sparrow = Sparrow() #자식 인스턴스 생성

my_chichken = Chicken() #자식 인스턴스 생성

my_sparrow.birdsong()  # 짹짹

my_chichken.birdsong() # 새소리



