# 1번째 문제 - 짝수는 싫어요
# 정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.
def solution(n):
    answer = []
    for i in range(n+1) :
        if i % 2 != 0 :
            answer += [i]
    return answer

# 다른 사람의 풀이
def solution(n):
    return [i for i in range(1, n+1, 2)]
    # 미리 변수를 선언할 필요 없고, 너도 for문 이렇게 한 줄에 쓸 줄 알아야 함. damn

# 2번째 문제 - 순서쌍의 개수
# 순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다.
# 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.

# 1번째 실행 - 틀림
def solution(n):
    answer = 0
    for a in range(1000) :
        for b in range(1000) :
            if a * b == n :
                answer += 1
    return answer
# 테스트 채점에서 성공으로 나와 맞췄다고 생각했지만 진짜 채점해보니 클림
# 어디가 잘못된 걸까 GPT에도 물어보고 계속 생각해보았으나 별다른 해결책을 얻지 못함
# 결국 구글링(..)

# 구글링하여 찾은 코드
def solution(n):
    answer = 0
    for i in range(1, n+1): # i가 1~n일 때
        if n % i == 0: # n이 i로 나누어 떨어지면. holly damn
            answer += 1
    return answer