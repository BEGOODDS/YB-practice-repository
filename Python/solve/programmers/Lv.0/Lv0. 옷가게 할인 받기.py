# 문제 설명
# 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다. 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.
# 제한 사항 - 10 ≤ price ≤ 1,000,000, 소수점 이하를 버린 정수를 return합니다.

# 풀이
# 조건문 활용
def solution(price):
    answer = 0
    if price >= 10 and price < 100000 :
        answer = int(price)
    elif price >= 100000 and price < 300000 :
        answer = int(price * 0.95)
    elif price >= 300000 and price < 500000 :
        answer = int(price * 0.9)
    elif price >= 500000 and price <= 1000000 :
        answer = int(price * 0.8)
    return answer

# 튜플을 사용하여 훨씬 정갈한 코드
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
