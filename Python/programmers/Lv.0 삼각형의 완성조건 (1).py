# 가장 긴 변이 나머지 두 변의 합보다 작아야한다는 삼각형의 조건을 만족시키는 함수를 만드는 문제
def solution(sides):
    answer = 0
    s = sorted(sides) # 오름차순 정렬
    a, b, c = s[0], s[1], s[2] # 각 변을 세 변수에 할당
    if c < (a + b) : # 삼각형 완성 조건 반영
        answer = 1
    else :
        answer = 2
    return answer
