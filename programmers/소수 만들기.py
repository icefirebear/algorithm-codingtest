# 첫번째 풀이 100
from itertools import combinations

def solution(nums):
    answer = 0
    nums_list = list(combinations(nums, 3))
    for num in nums_list:
        if isPrime(sum(num)):
            answer += 1
    return answer

def isPrime(data):
    for i in range(2, data//2):
        if data % i == 0:
            return False
    else:
        return True

# 두 번째 풀이 100
from itertools import combinations as cb

def solution(nums):
    answer = 0
    for num in cb(nums, 3):
        for i in range(2, sum(num) // 2):
            if sum(num) % i == 0:
                break
        else:
            answer += 1
    return answer
