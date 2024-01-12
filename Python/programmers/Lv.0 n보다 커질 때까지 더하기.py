def solution(numbers, n):
    answer = 0
    # 리스트 원소들을 하나씩 더하기
    for i in range(len(numbers)):
        # answer = 0 -> for문을 돌 때마다 answer이 0으로 초기화되므로 마지막 원소만 answer에 남게 됨
        answer += numbers[i]
        # if 문으로 조건 걸기
        if answer > n : # 원소들의 합이 n보다 커질 때
            return answer # 이때까지 더했던 원소들의 합 반환
    return answer
