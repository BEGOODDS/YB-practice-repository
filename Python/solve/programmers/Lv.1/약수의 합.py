# 문제 설명
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

def solution(n):
    answer = 0
    list_ = []
    for i in range(1, 3000) :
        if n % i == 0 :
            list_ += [i]
    answer = sum(list_)
    return answer # 정확도가 91.4임. 수정해야 함(..)