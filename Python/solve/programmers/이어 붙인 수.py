# 문제 설명
# 정수가 담긴 리스트 num_list가 주어집니다. num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.

# 최종 코드
def solution(num_list):
    answer = 0
    odd = ''
    even = ''
    for i in range(len(num_list)) :
        if num_list[i] % 2 != 0 :
            odd += str(num_list[i])
        else :
            even += str(num_list[i])
    list_ = [int(odd), int(even)]
    answer = sum(list_)
    return answer

# 최종 코드 작성 전 2번의 에러가 있었음
'''
1번째 에러 - TypeError: 'str' object is not callable
1번째 실행에서 변수명을 str로 잡는 실수를 했는데, 변수명을 str로 설정한 후 str()을 다시 호출할 때 발생하는 에러라고 한다.
밑의 코드처럼 말이다.
str += str(num_list[i])
해결책은? - str을 변수명으로 안 쓰면 된다.
가끔 실행 순서가 바꼈을 때 해당 에러가 나기도 한다고.
'''
'''
2번째 에러 - TypeError: int' object is not iterable
even과 odd를 int()안에 감싸준 후 sum()을 호출하니 해당 에러가 뜸.
그렇지(..) sum()은 문자열, 리스트와 같은 iterable 객체에만 사용가능한 함수이다.
해결책 - list에 even과 odd를 넣어 iterable로 만들어 준 후 sum() 호출
복습하자
'''