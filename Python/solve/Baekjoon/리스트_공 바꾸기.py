# 문제 설명
# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 바구니에는 공이 1개씩 들어있고, 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있다.
# 도현이는 앞으로 M번 공을 바꾸려고 한다. 도현이는 공을 바꿀 바구니 2개를 선택하고, 두 바구니에 들어있는 공을 서로 교환한다.
# 공을 어떻게 바꿀지가 주어졌을 때, M번 공을 바꾼 이후에 각 바구니에 어떤 공이 들어있는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
# 둘째 줄부터 M개의 줄에 걸쳐서 공을 교환할 방법이 주어진다. 각 방법은 두 정수 i j로 이루어져 있으며, i번 바구니와 j번 바구니에 들어있는 공을 교환한다는 뜻이다. (1 ≤ i ≤ j ≤ N)
# 도현이는 입력으로 주어진 순서대로 공을 교환한다.

# 출력
# 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다.

# 1번째 실행 - fail
# (리스트_공 넣기.py 파일에 있는) 공 넣기 문제 코드를 활용하여 코드를 구성
N, M  = map(int, input().split())
basket = [0 for _ in range(N)]
for m in range(N) :
    basket[m] = m+1
for k in range(M) :
    i, j = map(int, input().split())
    for n in range(M) :
        basket[i-1] = basket[j-1] # 이러면 하나만 바뀌는 건데 이걸 어떻게 고쳐야할지 몰랐음(..)(babo..)
        # basket[i-1], basket[j-1] = basket[j-1], basket[i-1] 원하는 요소 모두 바꾸는 코드
print(basket)

# 2번째 실행 - success
# GPT가 알려준 코드 중 일부를 반영하여 최종 코드 구성
N, M  = map(int, input().split())
basket = [0 for _ in range(N)]
for m in range(N) :
    basket[m] = m+1
for k in range(M) :
    i, j = map(int, input().split())
    # 1번째 실행 코드에 있는 중첩 반복문 내의 반복문 사용 시 공을 M번 바꾸게 됨
    # 문제의 조건은 1번만 교환하면 끝이어야 함
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

print(*basket) # 배열 변수명 앞에 *표시를 붙여주면 리스트의 각 요소만 출력해줌. 대박(..)