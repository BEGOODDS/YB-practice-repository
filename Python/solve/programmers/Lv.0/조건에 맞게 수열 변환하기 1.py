# 문제 설명
# 정수 배열 arr가 주어집니다. arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱합니다. 그 결과인 정수 배열을 return 하는 solution 함수를 완성해 주세요.

def solution(arr):
    answer = []
    for i in range(len(arr)) :
        if arr[i] >= 50 and  arr[i] % 2 == 0 :
            answer += [arr[i] // 2] # 다른 사람의 풀이에서 append를 쓴 코드가 많았음. answer.append(arr[i] // 2)
        elif arr[i] < 50 and arr[i] % 2 != 0 :
            answer += [arr[i] * 2]
        else :
            answer += [arr[i]]
    return answer
# 내 코드에선 += 을 사용하여 answer안에 넣어주려면 연산한 값을 꼭 []안에 넣어줘야 함.(그렇지 않으면 iterable 에러 발생)
# 리스트명.append(int)로 하면 그냥 int 값을 형변환 없이 넣어줄 수 있다. 이걸 이제(..)
# 수정한 버전
def solution(arr):
    answer = []
    for i in range(len(arr)) :
        if arr[i] >= 50 and  arr[i] % 2 == 0 :
            answer.append(arr[i] // 2)
        elif arr[i] < 50 and arr[i] % 2 != 0 :
            answer.append(arr[i] * 2)
        else :
            answer.append(arr[i])
    return answer