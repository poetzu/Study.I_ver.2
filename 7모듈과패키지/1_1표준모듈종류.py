

#표준 모듈 종류
# random모듈
# -> 랜덤값을 생성할떄 사용하는 모듈

#random모듈 불러오기
import  random
print("#random 모듈")

#random모듈의 random()함수는  0.0 <=  랜덤값  < 1.0 랜덤값을 float를 리턴합니다
print(random.random())

#random모듈의 uniform(min,max) 함수는 지정한 범위 사이의 랜덤값을 float를 리턴합니다
print(random.uniform(10,20))

#random모듈의 randranage()함수는 지정한 범위 사이의 랜덤값을 int로 리턴합니다
#문법) randrange(max) : 0부터 max값 사이의 랜덤값을 int로 리턴합니다
print(random.randrange(10))
#문법) randrange(min,max) : min값부터  max값사이의 랜덤값을 int로 리턴합니다
print(random.randrange(10,20))

#random모듈의 choice(리스트)함수는 리스트 내부에 있는 요소를 랜덤하게 선택합니다
print( random.choice([1,2,3,4,5]) )

#random모듈의 shuffle(리스트)함수는  리스트의 요소들을 랜덤하게 섞어서 제공해줌
list = ["ice cream", "pancakes", "brownies", "cookies", "candy"]
random.shuffle(list)
print(list)

#random모듈의 sample(리스트, k=숫자) 함수는
#리스트의 요소 중에  k개를 랜덤으로 뽑아냅니다
print( random.sample([1,2,3,4,5], k=2))

#예제. 계산 문제를 맞히는 게임  ->  random_1.py파일 생성
#예제. 타자 게임 -> typing.py파일 생성
#예제. 거북이 그래픽 모듈 사용하기 -> turtle_1.py 파일 생성  , turtle_2.py , turtle_3.py

#----------------------------------------------------------------------------

#sys 모듈
#-> 시스템과 관련된 정보를 가지고 있는 모듈

#모듈을 불러 옵니다
import sys

#컴퓨터 환경과 관련된 정보를 불러와 출력함
print(sys.getwindowsversion())
print("---")
print(sys.copyright)
print("---")
print(sys.version)

#프로그램을 강제로 종료 함
# sys.exit()

#---------------------------------------------------------------------

# os모듈
# ->  운영체제와 관련된 기능을 가진 모듈입니다
#     새로운 폴더를 만들거나  폴더 내부의 파일목록을 보는 일도 모두 os모듈을 활용해서 처리 합니다

#예제. 간단하게 os모듈의 몇가지 변수와  함수를 사용해 봅시다.

#모듈을 읽어 들입니다
import os

#기본 정보를 몇개 출력해 봅시다.
print("현재 운영체제 : ",  os.name)
print("현재 폴더 : ", os.getcwd())
print("현재 폴더 내부의 요소들(목록):",  os.listdir() )

#폴더를 만들고 제거합니다 [폴더가 비어있을때만 제거 가능]
#os.mkdir("hello") # hello폴더 생성
#os.rmdir("hello") # hello폴더 삭제

#파일을 생성하고 생성한 파일에 데이터를 씁니다.
# with open('original.txt','w') as file:
#     file.write("hello")

#파일 이름을 변경 합니다
#os.rename('original.txt','new.txt')

#파일을 제거 합니다
#os.remove('new.txt')

#--------------------------------------------------------------------

# datetime 모듈
# -> 날짜, 시간과 관련된 모듈로, 날짜형식을 만들때 사용되는 코드들로 구성되어 있는 모듈

#예제 .datetime모듈을 사용해서 날짜를 출력하는 다양한 방법

#모듈을 읽어들입니다
import datetime

#현재 시각을 구하고 출력하기
print("현재 시각 출력하기")

#datetime모듈. datetime클래스의 now()함수를 호출하여 현재 날짜와 시간정보를 모두 얻는다
now = datetime.datetime.now()
print(now.year,"년")
print(now.month,"월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

#시간 출력 방법
print("시간을 포맷에 맞춰 출력하기")

#현재 년도 월  일 시 분 초를 포맷에 맞춰서 출력하기
output_a = now.strftime("%Y.%m.%d %H:%M:%S")
print(output_a)

print("----------------------")

output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,
                                                now.month,
                                                now.day,
                                                now.hour,
                                                now.minute,
                                                now.second)
print(output_b)

print("-----------------------------")

# 문자열 ,리스트 등  앞에  별 *를 붙이면 요소 하나하나가 매개변수로 지정된다
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
print(output_c)

#결론 : output_a처럼 strftime()함수를 사용하면 시간을 형식에 맞춰 출력할 수 있습니다.
# 다만,  한국어등의 문자는 매개변수에 넣을수 없습니다.
# 그래서 이를 보완하고자 output_b 와 output_c같은 형식을 사용함

#특정 시간 이후의 시간 구하기
print("datetime모듈의 timedelta함수로 시간 더하기")
#timedelta함수를 사용하면 특정한 시간의 이전 또는 이후를 구할수 있습니다
#다만 1년 후 , 2년 후 등의 몇 년 후를 구하는 기능은 없습니다
#그래서 1년후를 구할때는 replace()함수를 사용해 아예 날짜 값을 교체하는 것이 일반적입니다
# 현재날짜시간정보에 +         1주일,  1일,     1시간,       1분,     1초
after = now + datetime.timedelta(weeks=1, days=1, hours=1, minutes=1, seconds=1  )

print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()

#특정시간 요소 교체하기
print("now.replace()함수로 1년 더하기")
output = now.replace(year=(now.year + 1))

print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()

#-----------------------------------------------------------------------

# time모듈
# -> 시간과 관련된 기능을 다룰때는 time모듈을 사용합니다
#    time모듈로 날짜와 관련된 처리를 할수 있지만, 그런처리는 datetime모듈을 사용하는 경우가 더 많습니다
# -> time모듈은 유닉스 타임(1970년 1월 1일 0시 0분 0초를 기준으로 계산한 시간단위)를 구할때
#    특정 시간 동안 코드 진행을 정지할때 많이 사용합니다

#예제 time모듈의  sleep()함수 사용해보기
#sleep(매개변수)함수는 특정 시간 동안 코드 진행을 저징할 때 사용하는 함수 입니다
#매개변수에는 정지하고 싶은 시간을 초 단위로 입력 합니다

import time

# print("지금 부터 5초 동안 정지 합니다")
# time.sleep(5)
# print("프로그램을 종료 합니다")
# start = time.time()
# print(start)

#---------------------------------------------------------------------

#urllib모듈
# -> 웹브라우저 주소창에 입력하는 인터넷 주소를 활용할때 사용하는 모듈입니다

#urllib모듈에 있는 request모듈을 읽어 들이자
from urllib import request

#request모듈 내부에 있는  urlopen()함수를 이용해서 구글의 메인 페이지의 코드 내용을 읽어 들입니다
#urlopen()함수는  URL주소의 페이지를 열어 주는 함수이다
#이렇게 입력하면 웹브라우저에 "https://google.com"을 입력해서 접속하는 것처럼
#파이썬프로그램이 "https://google.com"에 접속해 줍니다.
target = request.urlopen("https://google.com")

#이어서 read()함수를 호출하면 해당 웹 페이지에 있는 전체 소스 내용을 읽어서 가져옵니다
#urllib모듈의 request모듈의 urlopen()함수는 웹서버에 정보를 요청한 후, 돌려 받은 응답을 저장하여
#응답객체 HTTPResponse를 반환합니다.
#반환된 응답객체의 read()함수를 실행하여 웹 서버가 응답한 데이터를 바이트 배열로 읽어들입니다
#읽어들인 바이트 배열은 이진수로 이루어진 수열이어서 그대로는 사용하기 어렵다
#웹 서버가 응답한 내용이 텍스트 형식의 데이터라면, 바이트 배열의 decode('utf-8')메소드를 실행하여
#문자열로 변환할수 있다. 이때 utf-8 은 유니코드 부호화 형식의 한종류인데 decode()함수의 기본 인자이므로
#생략해도 된다.
output = target.read().decode("utf-8")

#읽어 드린 내용을 출력
print(output)

















































