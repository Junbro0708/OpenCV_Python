def solution(n):
    answer = 0
    for i in range(len(str(n))):
        answer += int(str(n)[i])
    return answer


def solution2(n):
    return sum([int(i) for i in str(n)])


print(solution2(123))
