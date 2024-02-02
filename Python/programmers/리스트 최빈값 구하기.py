# 문제 설명
# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다.
# 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요.
# 최빈값이 여러 개면 -1을 return 합니다.

# 처음엔 count 함수를 사용하여 코드를 구성해보았으나 실패
# count 함수는 특정 문자나 숫자열을 지정하지 않으면 TypeError가 발생함

# 결국 구글링
# collection 모듈의 counter 함수 활용
from collections import Counter

def solution(array):
    counts = Counter(array) # 각 값과 값의 개수가 들어있는 튜플 생성
    # most_common()을 활용하여 최빈값부터 먼저 정렬되는 리스트 생성
    common_list = counts.most_common()
    # chatGPT 활용 - 같은 값을 가진 키가 존재할 때 -1을 반환하는 if문 작성 요청
    most_common_count = common_list[0][1] # 최빈값
    # if문 - 값만 비교하기 때문에 for문에서 _을 사용하여 키 무시
    if any(count == most_common_count for _, count in common_list[1:]) :
        answer = -1
    else :
        answer = common_list[0][0]
    return answer