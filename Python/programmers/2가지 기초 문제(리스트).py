# 1번째 문제
# 두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

# 같은 원소의 '개수'가 도저히 감이 오지 않아 우선 같은 원소가 존재하면 1, 아니면 0 을 반환하도록 코드 구성
def solution(s1, s2):
    len_1 = len(s1)
    len_2 = len(s2)
    for i in range(len_1) :
        for j in range(len_2) :
            if s1[i] == s2[j] :
                return 1
            else :
                return 0
# 하지만 이렇게 하면 s1의 길이가 s2의 길이보다 짧을 경우 제대로 실행되지 않음
# 문제의 제한 사항에 따라 반복문 수정
def solution(s1, s2):
    for i in range(100) :
        if s1[i] == s2[i] :
            return 1
        else :
            return 0
# 근데 이래도 1이 반환되지 않음. 

# 결국 코드 구글링(..)
def solution(s1, s2):
    answer = 0
    for i in s1: # i가 s1에 있는 동안
        if i in s2: # i가 s2에 있다면
            answer += 1 # 그 수 만큼 answer에 1씩 더한다
    return answer

# 반복문, 조건문 응용이 아직도 많이 약한 것 같음
# 이런 문제들을 찾아 풀어야 함

# set()함수와 교집합을 이용하여 두 줄로 만든 코드도 있음 ..ㄷ
def solution(s1, s2):
    return len(set(s1)&set(s2)); # set() 함수 - 집합 자료형을 만들 수 있는 함수, 순서가 없고 중복을 허용하지 않음

# 2번째 문제
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

# 스스로 풀긴 했으나 한 방에 풀진 못함
# 전역 변수 answer을 선언하지 않은 상태에서 반복문에 += 연산자를 사용하였다가 local variable 에러가 남
def solution(numbers):
    len_ = len(numbers)
    answer = []
    for i in range(len_) :
        answer += [numbers[i]*2]
    return answer

# 다른 사람의 풀이
def solution(numbers):
    return [num*2 for num in numbers] # 반복문을 이렇게 한 줄에.. ㄷ
# 찾아보니 이것이 '리스트 내포'라고 함
# [표현식 for 항목 in 반복 가능 객체 if 조건] , if문은 생력 가능.
