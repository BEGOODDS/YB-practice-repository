# 문제 설명
# 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

# 문제의 my_string은 'h4j56k'와 같은 문자와 숫자를 함께 포함한 문자열
# '입력한 것 중 숫자만 뽑아내어 더하기'를 하고 싶었으나 혼자 힘으로는 실패
# with GPT
def solution(n):
    int_list = [int(char) for char in n if char.isdigit()]
    return sum(int_list)

# for, if 문 한 줄에 쓸 수 있음(언제쯤 할 수 있을까)(..)

# isdigit() - 문자열이 모두 숫자인지 판별하는 메서드
# 문자열을 순회하면서 문자열에 숫자만 존재하면 True, 문자가 존재하면 False를 반환
# 위 코드에서는 조건문에 사용하여 문자열에 숫자가 존재할 경우 해당 문자를 정수로 변환하여 리스트에 들어갈 수 있게 함
# 요물이네