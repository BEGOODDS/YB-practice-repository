# 문제 설명
# 자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.

# 1번째 실행 - 범위 실수
def solution(n):
    answer = 0
    for x in range(3, 10000000) : # x의 범위를 n의 범위로 설정하는 실수를 범함(..) - 태스트 케이스는 맞추는데, 정확도가 떨어져 자꾸 틀리게 됨.
        if n % x == 1 :
            answer = x
            break
    return answer

# 최종 코드 - 프로그래머스 각 문제에 있는 질문하기 게시판에서 다른 사람이 범위 설정한 것을 보고 고침. 맞음(..)
def solution(n):
    answer = 0
    for x in range(1, n) : # damn
        if n % x == 1 :
            answer = x
            break
    return answer