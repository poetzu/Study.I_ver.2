

# 사용할 모듈을 불러옵니다

#urlopen함수는  url에 접속하기 위한 함수이다.
#웹크롤링을 위해서 반드시 사용해야 하는 함수 이다.
#from문은 특정 라이브러리에서  한 부분만을 불러와서 사용할 때 사용하는 구문이다.
#urllib.request모듈 내부에 있는 urlopen이라는 함수만 불러와서 사용하겠다는 내용이다.
from urllib.request import urlopen

#bs4모듈의 BeautifulSoup클래스를 사용하기 위해 불러옵니다
from bs4 import BeautifulSoup


#request모듈 내부에 있는 urlopen()함수를 이용해 기상청 페이지의 코드 내용을 읽어 들입니다
#urlopen()함수는 URL주소의 페이지를 열어주는 함수 입니다.
#urlopen()함수로 기상청의 전국 날씨를 제공하는 사이트를 열어주고 read()함수로 데이터들을 읽어들입니다.
#decode()함수로 읽어 들인 바이너리 데이터를 문자열로 변환해서 얻습니다.
target = urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108").read().decode('utf-8')
#urllib.request.urlopen()함수는 웹 서버에 정보를 요청한 후, 돌려 받은 응답을 저장하여
#응답 객체(HTTPResponse)를 반환한다.
#반환된 응답 객체의 read()메소드를 실행하여 웹 서버가 응답한 데이터를 바이트 배열로 읽어 들인다
#읽어들인 바이트 배열은 이진수로 이루어진 수열이어서 그대로는 사용하기 어렵다.
#웹서버가 응답한 내용이 텍스트 형식의 데이터라면,
# 바이트 배열의 decode("utf-8")메소드를 실행 하여 문자열로 변환할수 있다.

#BeautifulSoup을 사용해 웹 페이지를 분석합니다
#target변수에 저장된 값들(읽어들인 전체 내용 html문자열)과, "html.parser"라는 문자열을
#BeautifulSoup()함수의 매개변수로 넣어주면
#읽어들인 전체 HTML내용중 특정 부분의 데이터를 파씽 할수 있는 역할을 하는 BeautifulSoup객체로 만들어 줌으로써
#BeautifulSoup객체의 유용한 메소드(원하는 데이터 추출)를 사용하여 데이터를 뽑아 낼수 있다.
soup = BeautifulSoup(target, "html.parser")

#유용한 함수
#select("선택하여 가져올 태그명") 함수
# -> HTML전체 데이터 중에서.. select함수 호출시 인수로 전달한 태그명에 해당 되는 태그들만 추출해서
#    새로운 배열에 모두 담아 배열을 반환 해주는 함수 이다.

#모든? <ctiy>..</city> 태그들을 선택하여 새로운 배열(리스트)에 담아 리스트를 반환해줌
# cityTagsList = soup.select("city")
# print(cityTagsList)

# select("location") 메소드는 읽어 들인 전체 HTML내용중....
# <location>....</location>태그 한쌍씩  모두 찾아서 ... 새로운 리스트에 각각 저장 후
# 리스트 자체를 반환 해 준다.
for location in soup.select("location"):
    #<location>...</location>태그 내부의  <city></city> , <wf></wf>, <tmn></tmn> , <tmx></tmx>태그들을
    #각각 선택해서  텍스트 노드 값만? 얻어서 출력
    print("도시 : ", location.select_one("city").text)
    print("날씨 : ", location.select_one("wf").string)
    print("최저기온 : ", location.select_one("tmn").string)
    print("최고기온 : ", location.select_one("tmx").string)
    print()

#select_one() 메소드
# 만족하는 첫번째 경우의 태그요소만 찾아서 반환 시킨다.














