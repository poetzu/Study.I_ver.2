
#딕셔너리란?
#리스트와 튜플등에서는 정수인 인덱스(index)를 가지고 순차적으로 각 요소에 접근 할수 있었다면,
#딕셔너리는 단어 그대로 '사전'과 같이 별도로 정의 키(key)를 통해 각 요소에 접근할수 있도록 만들어진 데이터타입이다

#딕셔너리 선언 하기 문법
#딕셔너리명 = {요소1,  요소2,  요소3,....}
#요소 = 키(key) : 값(value)

#설명 : 딕셔너리는 중괄호 {}로 깜사서 선언 하며, 딕셔너리의 각 요소들은 쉼표,를 사용 하여 구분 합니다.
#       이러한 딕셔너리의 요소는 또 다시 key와 value의 한쌍으로 구성되며 이둘은 콜론 : 으로 연결 됩니다.

#딕셔너리 만들기 예제
dic = {'name':'pey', 'phone':'010', 'birth':'1118'}
#     {   key:value,   key: value,   key:value}

#딕셔너리 데이터를 쌍으로 추가하는 예제
a = {1:'a'}

a[2] = 'b' #{2:'b'} 쌍 추가
print(a)   #{1:'a',2:'b'}

a['name'] = 'pey'   #딕셔너리a에  'name':'pey'라는 쌍을 추가 시킴
print(a)   #{1:'a', 2:'b', 'name':'pey'}

a[3] = [1,2,3]  #딕셔너리a에  key는 3, value는 [1,2,3]을 가지는 한쌍을 추가 시킴
print(a)  #  {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

#딕셔너리 요소 삭제 하기 예제
#del 함수를 사용해서 del a[key]처럼 입력하면  지정한 key에 해당하는 {key:value}쌍이 삭제 된다.

#key가 1인  key:value를 쌍으로 삭제
del a[1]
print(a)  # {2: 'b', 'name': 'pey', 3: [1, 2, 3]}

#딕셔너리에서 key를 사용해 value 얻기
#예제
grade = {'pey':10, 'julliet':99}
#key가 'pey'인 딕셔너리의 value 10을 되돌려 받자
print(grade['pey'])
print(grade['julliet'])

#딕셔너리 관련 함수
#딕셔너리를 자유자재로 사용하기 위해 딕셔너리가 자체적으로 가지고 있는 관련 함수를 사용 해보자.

#1. key들을 요소로 갖는 리스트 만들기
#예제
a = {'name':'pey', 'phone':'011', 'birth':'1118'}
d = a.keys()  # 딕셔너리a의 key값들만 모아서  dict_keys객체에 저장한 후 반환해 줍니다.
print(d)  #  dict_keys(['name', 'phone', 'birth']) 객체가 출력됨

#참고 dict_keys객체를 리스트로 변환하려면?
list = list(a.keys())
print(list)  # ['name','phone','birth'] 리스트 객체 출력됨

#2. value들을 요소로 갖는 리스트 만들기
#key를 얻는것과 마찬가지 방법으로  value만 얻고 싶다면  value함수를 사용하면 된다.
a = {'name':'pey', 'phone':'011',  'birth':'1118'}
d = a.values()
print(d)  # dict_values(['pey', '011', '1118']) 객체가 출력됨
# list = list(a.values())
# print(list)

#3. key,value쌍으로 얻기(items함수 사용)
# items함수는 key와 value의 쌍을  튜플로 묶은 값을  dict_items객체로 돌려준다.
#예제
a = {'name':'pey', 'phone':'011',  'birth':'1118' }
b = a.items()
print(b)  # dict_items([('name', 'pey'), ('phone', '011'), ('birth', '1118')]) 출력됨

#4. key:value쌍 모두 지우기
# clear함수는 딕셔너리 안의 모든 요소를 삭제 한다.
# 빈 리스트를 [], 빈튜플을 () 로 표현하는 것과 마찬가지로 빈 딕셔너리도 {}로 표현한다.
#예제
a = {'name':'pey', 'phone':'011',  'birth':'1118' }
a.clear()
print(a)  # {} 빈 딕셔너리 출력됨

#5. key로 value얻기
#  get(x)함수는  x라는 key에 대응 되는 value를 돌려 준다.
#예제
a = {'name':'pey', 'phone':'011'}
b = a.get('name')
print(b)  # pey 출력됨

#6. 해당 key가 딕셔너리 안에 있는지 조사하기
#  in 키워드를 사용한다
#예제
a = {'name':'pey', 'phone':'011'}
b = 'name' in a  #'name' in  a를 호출하면 참(True)을 돌려 준다
print(b) # True




































