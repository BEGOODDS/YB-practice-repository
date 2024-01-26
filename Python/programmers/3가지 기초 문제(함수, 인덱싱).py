# 1번째 문제 - 문자열 뒤집기
# 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.

# 구글링 - 문자열에 reverse라는 메서드가 존재하지 않는다는 것을 몰랐음
# reverse를 사용하려면 문자열을 리스트로 변경하여 reverse 사용 후 다시 변경해주어야 함

# 다른 방식인 인덱싱으로 하는 것이 코드를 간결하게 구성할 수 있는 방법
def solution(my_string):
    return my_string[::-1]

# reverse 활용 코드
def solution(my_string):
    answer = list(my_string)
    answer.reverse()
    # 뒤집기한 리스트를 문자열로 바꾸려면 join 함수를 활용해야 함
    answer = str(answer)
    return answer


# 2번째 문제 - 리스트 중앙값 구하기
# 중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다. 예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 
# 정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.

# 내 힘으로 한 방에 풀지 못함
# 구글링으로 중간값을 구하는 코드를 보고 인덱싱을 활용
def solution(array):
    # 오름차순 정렬
    array.sort()
    return array[len(array)//2]

# 다른 사람의 풀이

def solution(array):
    return sorted(array)[len(array) // 2] # sorted(리스트명)[인덱스]하니 더 코드가 더 간결함


# 3번째 문제 - 문자열에서 특정 문자 제거하기
# 문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

# 마찬가지 구글링(..)
# del() 함수를 쓰면 되지 않을까 싶었는데 정확한 사용법을 몰랐음

# del() 함수 
# 문자열의 일부 원소 삭제 기능은 제공하지 않음
# 리스트에서도 사용하려면 인덱싱을 활용해서만 일부 원소 삭제 가능함

# 결국 replace() 함수 사용
# 변수명.replace('삭제 문자','')
def solution(my_string, letter):
    return my_string.replace(letter,'')
