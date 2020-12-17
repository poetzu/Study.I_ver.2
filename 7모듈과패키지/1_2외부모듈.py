

# 외부 모듈이란?
# - 파이썬에서 기본적으로 제공해 주는 것이 아니라,...
#  다른 사람들이 만들어 배포하는 모듈을 외부모듈이라 부릅니다
#  서점에 가면 파이썬 도서를 둘러보면  사이킷-런 , 텐서플로우, 쟁고, 플라스크, 넘파이 등이라고 적혀 있는 책을
#  볼수 있는데 이러한 책들은 모두 다른 사람들이 만들어서 제공해 주는 외부 모듈에 관한 책입니다.

# Beautiful Soup 외부 모듈이란?
# - beautifulsoup은 html의 태그를 다룰 수 있는 라이브러리로...
#   html태그를 함수를 이용해서 필요한 정보들을 쏙쏙 뽑아낼(파싱)수 있게 도와주는 외부 모듈(라이브러리) 이다.

# 주제1. Beautiful soup외부모듈을 설치하고 사용하는 기본적인 방법을 알아 봅시다.

# 뷰티풀 숩 외부 모듈의 공식 홈페이지
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

#순서1. 뷰티풀 숩 외부 모듈을 설치 하기 위해 윈도우 운영체제에서 Window + R키를 눌러
#      프로그램 실행창을 뛰우고  cmd명령을 입력하여 명령프롬포터 창을 띄웁니다

#순서2. 명령프롬포터 창에 다음과 같이 입력하여 뷰티풀 숩 외부 모듈 설치합니다
# pip install beautifulsoup4

#순서3. BeautifulSoup모듈을 사용해서  기상청의 날씨 정보를 가져와 출력 해보기 위해
#  https://www.weather.go.kr/weather/lifenindustry/sevice_rss.jsp 사이트에 접속합니다.

#순서4. 웹브라우저에 나타난 화면중..
# 중기예보 > 전국 RSS클릭 >
# http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108
# 메모장에 복사 해 놓기

#순서5. BeautifulSoup외부모듈로 기상청의 실시간 전국날씨를 읽어 오기 위해
# beautiful_weather.py 파일 만들기















