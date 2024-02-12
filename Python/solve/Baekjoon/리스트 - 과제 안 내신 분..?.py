# 문제 설명
# X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
# 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

# 입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.

# 출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.

# 변수 설정
students = [i+1 for i in range(30)]
students_submit = list(int(input()) for _ in range(28))
'''
students_submit - 처음엔 map을 사용함.
그러나 map을 사용할 때 입력한 문자열을 하나씩 리스트에 넣으려면 split()을 사용해야 하고,
split() 사용 시 공백을 기준으로 분할하기 때문에 문제의 입력 조건과 맞지 않음
추가적으로 split()이 공백을 기준으로 분할하므로 반복문과 함께 써도 원하는 리스트를 얻을 수 없음(각 요소가 map이 됨)
'''

# 조건문
# students의 요소들 중 students_submit에 존재하지 않는 요소를 출력
# while문, for문 등 여러 시도를 해보았으나 실패(hunghung)

# with GPT(..)
for element in students: # students의 요소들 중
    if element not in students_submit: # students_submit에 포함되지 않은 요소가 있다면
        print(element) # 해당 요소 출력..이렇게 간단하다고(..?)

# 여러 시도 중 답과 가장 근접했던 내 코드 - error
for i in range(30) :
    if students[i] not in students_submit[i]:
        print(students[i])
'''
GPT : 'students와 students_submit의 인덱스를 동시에 사용하여 요소를 비교하려고 시도했기 때문에 에러가 난 것.
두 리스트를 각각 순회하여 비교해야 함'
'''