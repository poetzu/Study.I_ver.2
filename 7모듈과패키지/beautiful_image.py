
# [파이썬 웹 크롤링]  BeautifulSoup를 이용한 웹크롤링  - 사진 다운로드

#파이썬 urllib모듈을 이용하여 웹상에서 사진을 가져오는 방법에 대한 설명

#-------------------이미지 다운로드 하기----------------
#크롤링을 하기 전에 알아야 할것은 이미지가 웹상 특정 경로에 존재 하는지에 관한 유무 입니다.
#사진을 크롤링 하기 위하여 네이버 영화의 마약왕 영화 리뷰 사이트를 참고 합시다.

#사이트 링크 : https://movie.naver.com/movie/bi/mi/basic.nhn?code=15729
#
# 사이트에 접속하면 마양와 사진이 노출되어 있는가를 확인하고
# 마양왕 사진의 URL경로 확인을 위해 F12 키를 눌러 개발자 도구 창을 활성화 시킨뒤
# 개발자 도구의 왼쪽 상단 맨 위쪽에  위치한 화살표 버튼을 클릭하고
# 소스를 알고 싶은 웹페이지의 부분을 클릭하면  자동으로 마약왕 사진이 위치한 소스영역을 보여주게 됩니다.


import urllib.request
from bs4 import BeautifulSoup

print("Beginning file download with urllib2.......")

#request모듈 내부에 있는 urlopen()함수를 이용해 페이지의 코드 내용을 읽어 들입니다.
url = "https://movie.naver.com/movie/bi/mi/basic.nhn?code=157297"
res = urllib.request.urlopen(url).read()

#읽어들인 전체HTML소스중에서 특정 부분의 코드를 파싱하기 위해
#BeautifulSoup객체 생성
soup = BeautifulSoup(res, "html.parser")

#읽어들인 전체HTML소스중에서 class속성값이  poster인  div요소영역만 추출함
soup = soup.find("div", class_="poster") #find()메소드를 이용하여 원하는 요소영역만 추출함!
# <div class="poster">
#     <a href="#"
#        onclick="javascript:common.iwopen('157297');clickcr(this,'ifo.img','','',event);return false;">
#        <img alt="마약왕"
#             onerror="this.src='https://ssl.pstatic.net/static/movie/2012/06/dft_img77x110_1.png'"
#             src="https://movie-phinf.pstatic.net/20181126_96/1543207321602QPWG8_JPEG/movie_image.jpg?type=m77_110_2"/>
#        <span>포스터 크게보기</span>
#     </a>
# </div>

# 파씽한 <div> <img> </div>소스 중에서 <img>요소의 src경로만 찾아서 가져 옵니다
imgUrl = soup.find("img")["src"]
print(imgUrl)
# https://movie-phinf.pstatic.net/20181126_96/1543207321602QPWG8_JPEG/movie_image.jpg?type=m77_110_2

#urlretrieve(다운로드할 URL,경로 및 파일명)함수는 다운로드 역할을 하는 함수
urllib.request.urlretrieve(imgUrl, soup.find("img")["alt"] + '.jpg') # img.alt는 이미지 명 == 마약왕












