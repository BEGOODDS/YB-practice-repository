# 문제 설명
# 알파벳으로 이루어진 문자열 myString이 주어집니다.
# 모든 알파벳을 대문자로 변환하여 return 하는 solution 함수를 완성해 주세요.

def solution(myString):
    return myString.upper()

# 문제 설명
# 문자열 my_string과 정수 n이 매개변수로 주어질 때,
# my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.

# 1번째 코드
def solution(my_string, n):
    return my_string * n
# 이 상태에서 같은 문자끼리 묶어주는 방법을 모르겠음

# 2번째 코드
def solution(my_string, n):
    my_string_len = len(my_string)
    a = ''
    for i in range(0, my_string_len) :
        # a = '' - 이 부분 때문에 결과가 자꾸 안 나오는 거였움. 변수 여기서 선언하면 반복문 실행할 때마다 초기화된다(ㅜㅜ)
        a += my_string[i] * n # 하나씩 더해서 넣어줘야 함
    return a

# 문제 설명
# 어떤 세균은 1시간에 두배만큼 증식한다고 합니다.
# 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.

def solution(n, t):
    for i in range(t):
        n += n
    return n

# 문제 설명
# 양의 정수 n이 매개변수로 주어질 때, 
# n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.

def solution(n):
    answer = 0
    a = 0
    if n % 2 != 0 :
        for i in range(n) :
            # n 이하의 홀수들의 합
            if i < n and i % 2 != 0 :
                n += i
        return n
    else :
        b = 0
        for i in range(n) :
            if i < n and i % 2 == 0 :
                a = n ** 2
                b += i ** 2
                # 처음엔
                # b = i ** 2 후
                # a += b 이렇게 함 - 가만히 노려보다가(..) 이러면 b에 제곱수들이 더해지지 않는다는 것을 깨달음 :-(
        return a + b

# 훨씬 간단한 코드
def solution(n):
    if n % 2:
        return sum(range(1,n+1,2)) # range에서 간격 설정 후 sum.. 대박
    return sum([i*i for i in range(2,n+1,2)])
