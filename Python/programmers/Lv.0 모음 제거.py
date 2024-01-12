def solution(my_string):
    # 모음으로 이루어진 리스트 생성
    vowel = ['a', 'e', 'i', 'o', 'u']
    # answer이 모음을 제외하도록 코드 구성
    for _ in vowel :
        answer = my_string.replace(_, '')
    # 위 코드 실행 결과 리스트 속의 모든 요소들이 결과에 적용되지 않음
    
    # 여러 문자열을 매개변수로 받는 함수 or 여러 문자를 한 번에 삭제할 수 있는 방법이 필요
    # replace 함수 - 여러 번 겹쳐 쓸 수 있어 이를 활용하여 모음 삭제(매개변수는 2가지만 사용 가능)
    answer = my_string.replace('a', '').replace('e','').replace('i', '').replace('o', '').replace('u', '')
    return answer
