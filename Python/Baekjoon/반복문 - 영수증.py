# 영수증 - 반복문 활용 문제

# 준원이가 코스트코를 갔다고 함
# 근데 몇 개 담지도 않았는데 수상하게 높은 금액이 나왔다고 함(너가 많이 사서 그랬갰지 준원아(..))
# 첫째 줄에 영수증에 적힌 총 금액 X, 둘째 줄에 영수증에 적인 물건 종류의 수 N,
# 이후 N개의 줄에 각 물건 가격 a와 개수 b가 공백을 사이에 두고 주어질 때,
# 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes, 아니면 No를 출력하는 문제

# 1번째 실행 - error
X = int(input())
N = int(input())
for i in range(N) :
    a, b = map(int,input().split())
if sum(a * b) == X :
    print('Yes')
else :
    print('No')
# TypeError: 'int' object is not iterable
# 꽤 많이 본 에러인데 iterable 자료형을 몰라 구글링
# iterable - member를 하나씩 차례로 반환 가능한 객체
# str, list, tuple, range, set, dictionary가 여기에 해당

# 2번째 실행
# 가격 합계를 iterable 중 list형으로 변경하는 코드
X = int(input())
N = int(input())
list = [] # 많이 했던 실수(반복문 안에 전역 변수 선언) 개선(부끄럽다)
for i in range(N) :
    a, b = map(int,input().split())
    list += [a * b]
if sum(list) == X :
    print('Yes')
else :
    print('No')