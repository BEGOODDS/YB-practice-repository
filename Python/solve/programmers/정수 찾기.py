# 문제 설명
# 정수 리스트 num_list와 찾으려는 정수 n이 주어질 때, num_list안에 n이 있으면 1을 없으면 0을 return하도록 solution 함수를 완성해주세요.

def solution(num_list, n):
    answer = 0
    if n in num_list :
        answer = 1
    return answer