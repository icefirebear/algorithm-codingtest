# 1차 시도: 43

# 풀이: 정규식을 통해 첫글자가 숫자인지 판별하였다. 테스트 케이스는 통과하였지만 제출하였더니 많이 틀렸다.
import re


def solution(s):
    answer = [
        word.title() if not re.match("[0-9]", word[0]) else word for word in s.split()
    ]
    return " ".join(answer)


# 2차 시도: 43
# 풀이: 정규식 사용에서 문제가 있었나라고 생각이 들어 ord()를 사용해 ASCII 값으로 판별하였지만 점수는 똑같았다.
def solution(s):
    answer = [
        word.title() if not 48 <= ord(word[0]) <= 57 else word.lower()
        for word in s.split()
    ]
    return " ".join(answer)


# 3차 시도: 100
# 풀이: lower()와 capitalize()를 사용해 첫글자 대문자+뒤문자들 소문자 형태로 변형을 수행하였고 split()의 조건을 " "으로 한정하였습니다.
def solution(s):
    return " ".join([word.lower().capitalize() for word in s.split(" ")])
