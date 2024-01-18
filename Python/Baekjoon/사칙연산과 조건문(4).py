# 사칙 연산

# 1번째 문제 설명
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 두 정수를 공백 기준으로 입력해야 함 - split 함수
# 입력된 데이터는 문자열이므로 map 함수를 활용하여 int로 변환
# sum - 더하기
print(sum(map(int, input('').split())))
# 더하기를 제외한 나머지 연산은 모두 연산자를 써야 함

# 2번째 문제 설명
# 불교 국가인 태국은 불멸기원(佛滅紀元), 즉 석가모니가 열반한 해를 기준으로 연도를 세는 불기를 사용한다. 반면, 우리나라는 서기 연도를 사용하고 있다.
# 불기 연도가 주어질 때 이를 서기 연도로 바꿔 주는 프로그램을 작성하시오.

# 어려워 보였으나 그냥 빼기 문제였음
a = int(input(''))
print(a-543)

# 조건문

# 1번째 문제 설명
# 흔한 수학 문제 중 하나는 주어진 점이 어느 사분면에 속하는지 알아내는 것이다. 사분면은 아래 그림처럼 1부터 4까지 번호를 갖는다. "Quadrant n"은 "제n사분면"이라는 뜻이다.
# 점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오.

a, b = int(input('')), int(input(''))
if a > 0 and b > 0 :
    print('1')
elif a < 0 and b > 0 :
    print('2')
elif a < 0 and b < 0 :
    print('3')
else :
    print('4')

# 2번째 문제 설명
# 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 
# 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.

# 변수 선언
hour, min = map(int, input('').split())
time = int(input(''))

# 1번째 실행
# 변수를 하나 더 만들어서 현재 '분'과 '요리 시간' 더한 후
min_ = min + time
# 해당 변수가 60 이상인 경우와 아닌 경우로 나눔
if min_ >= 60 :
    if hour >= 24 :
        hour, min = 0, time - (60 - min)
        print(hour, min)
    else :
        hour, min = hour + 1, time - (60 - min)
        print(hour, min)
else :
    print(hour, min_)
# 그냥 예시 맞춤용 코드를 만들어버린 것
# 심지어 두 번째 예시에는 맞지 않음

# 2번째 실행
# hour를 기준으로 24보다 큰지, 작은지에 따라 나눔
if hour < 24 :
    if min_ < 60 :
        print(hour, min_)
    elif min_ >= 60 :
        hour = hour + 1
        min =
        print(hour, min)
elif hour >= 24 :
    if min_ < 60 :
        hour = 0 + 1
# 도저히.. 떠오르지 않음

# 결국 코드 전체 구글링..
H, M = map(int, input().split())
timer = int(input())

H += timer // 60 # 몫만 내는 연산자로 하면 2시간이든 3시간이든 더할 수 있구나..
M += timer % 60 # 나머지로.. 대박
# 이렇게 하고 가면 조건문을 진짜 간단하게 써도 됨

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M) # 멀었다 YB.,화팅
