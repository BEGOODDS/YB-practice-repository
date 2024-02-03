# 문제 설명
# 단어가 공백 한 개로 구분되어 있는 문자열 my_string이 매개변수로 주어질 때,
# my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.

def solution(my_string):
    return my_string.split() # split() 함수 - 문자열을 공백 기준으로 나누어 줌

# 문제 설명
# 정수 리스트 num_list와 정수 n이 주어질 때,
# n 번째 원소부터 마지막 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성해주세요.

def solution(num_list, n):
    return num_list[n-1:] # list slicing

# 문제 설명
# 'm'과 "rn"이 모양이 비슷하게 생긴 점을 활용해 문자열에 장난을 하려고 합니다.
# 문자열 rny_string이 주어질 때, rny_string의 모든 'm'을 "rn"으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.

def solution(rny_string):
    return rny_string.replace('m', "rn") # replace(,) 함수 - 말 그대로 그냥 대체

# 문제 설명
# 정수 리스트 num_list와 정수 n이 주어질 때,
# num_list를 n 번째 원소 이후의 원소들과 n 번째까지의 원소들로 나눠 n 번째 원소 이후의 원소들을 n 번째까지의 원소들 앞에 붙인 리스트를 return하도록 solution 함수를 완성해주세요.

# 한 번에 못 풀음
# 구글링 중 리스트를 분할하는 코드에서 인덱싱과 반복문을 사용한 것을 보고 아이디어를 얻음
def solution(num_list, n):
    return num_list[n:] + num_list[:n] # list slicing, list chunk

# 문제 설명
# 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다.
# 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 2 * a * b 중 더 큰 값을 return하는 solution 함수를 완성해 주세요.
# 단, a ⊕ b와 2 * a * b가 같으면 a ⊕ b를 return 합니다.

def solution(a, b):
    sum = int(str(a) + str(b))
    mul_2ab = 2 * a * b
    if mul_2ab > sum :
        return mul_2ab
    elif sum >= mul_2ab :
        return sum

# max() 함수를 이용한 훨씬 간단한 코드를 발견함
def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b) # max() 함수 - 쉼표를 사용하여 여러 수들 중 가장 큰 수를 출력

# 문제 설명
# 문자열 배열 strlist가 매개변수로 주어집니다.
# strlist 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.

# 첫번째 풀이
def solution(strlist) :
    for i in range(len(strlist)) :
        len_list = [len(strlist[i])]
        i += 1 # for문이면 알아서 늘어나는데 뻘짓을 함
        len_list += [len(strlist[i])] # 뻘짓 2 - append가 아닌 이상한 방법으로 더하려 함

    return len_list # 당연히 실패

# 두번째 풀이(with chatGPT ..) 이렇게 간단한 코드였음
def solution(strlist):
    len_list = []
    for i in range(len(strlist)):
        len_list.append(len(strlist[i])) # append()..
    return len_list
