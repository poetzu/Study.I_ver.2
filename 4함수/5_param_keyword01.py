
#함수 호출시 매개변수 이름을 직접적으로 지정해서 값을 입력하여 전달 받는 매개변수를 키워드 매개변수라 부른다

def print_n_times(*values,n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

#함수를 호출합니다
print_n_times("안녕하세요","즐거운","파이썬 프로그래밍",n=3) #매개변수 이름n에 직접적으로 값을 저장하여 전달함
                                                        #n=3 자체를? 키워드 매개변수라고 부른다
