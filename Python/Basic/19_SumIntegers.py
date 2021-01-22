def solution(a, b):
    answer = 0
    if a <= b:
        for i in range(a, b + 1, 1):
            answer += i
    elif a >= b:
        for i in range(b, a + 1, 1):
            answer += i
    return answer


def solution(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


print(solution(3, 5))
