print("x와 n을 입력해주세요.")
x = int(input())
n = int(input())

print("x = {} n = {}".format(x, n))


def solution(x, n):
    answer = []
    if x == 0:
        for i in range(0, abs(n), 1):
            answer.append(x)
    else:
        for i in range(x, x * (n+1), x):
            answer.append(i)
    return answer


print(solution(x, n))
