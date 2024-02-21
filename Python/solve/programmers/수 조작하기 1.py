# 문제 설명
# 정수 n과 문자열 control이 주어집니다. control은 "w", "a", "s", "d"의 4개의 문자로 이루어져 있으며, control의 앞에서부터 순서대로 문자에 따라 n의 값을 바꿉니다.
# "w" : n이 1 커집니다.
# "s" : n이 1 작아집니다.
# "d" : n이 10 커집니다.
# "a" : n이 10 작아집니다.
# 위 규칙에 따라 n을 바꿨을 때 가장 마지막에 나오는 n의 값을 return 하는 solution 함수를 완성해 주세요.

# 문제를 이해하는데에 시간이 걸렸어서 입출력 예시도 작성해놓는다.
# 입출력 예시
# n = 0 이고 control = "wsdawsdassw" 일 때,
# 수 n은 control에 따라 다음과 같은 순서로 변하게 됩니다.
# 0 → 1 → 0 → 10 → 0 → 1 → 0 → 10 → 0 → -1 → -2 → -1
# 따라서 -1을 return 합니다.

def solution(n, control):
    answer = 0
    w, s, d, a = control.count("w"), control.count("s"), control.count("d"), control.count("a")
    answer = n + (1 * w) - (1 * s) + (10 * d) - (10 * a)
    return answer

# 다른 사람의 풀이에서 본 튜플을 이용한 코드
def solution(n, control):
    answer = n
    c = { 'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        answer += c[i]
    return answer # 코드가 진짜 한 눈에 들어온다.