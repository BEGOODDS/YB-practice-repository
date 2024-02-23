# 문제 설명
# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요.

def solution(n):
    str_list = list(''.join(str(n))) # join - iterable 타입만 사용 가능
    int_list = list(map(int, str_list))
    return sum(int_list)

# 근데 이렇게 join을 써서 list로 설정할 필요 없이,
# 그냥 str(n)만 한 후 int로 형 변환하여 더해도 됨.
# 다른 사람의 풀이
def solution(n):
    answer = sum(list(map(int, str(n))))
    return answer