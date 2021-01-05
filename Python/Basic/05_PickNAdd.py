def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    for i in range(len(answer) - 1):
        for j in range(i + 1, len(answer)):
            if answer[i] > answer[j]:
                src = answer[i]
                answer[i] = answer[j]
                answer[j] = src
            else:
                pass
    # sorted 함수 사용하면 한줄 요약 가능

    for i in range(len(answer) - 1):
        for k in range(0, len(answer) - 1, 1):
            if answer[k] == answer[k + 1]:
                answer.pop(k + 1)
                break

    return answer
    # set 로 형변환하면 한줄 요약 가능


def solution1(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))


print(solution([5, 0, 2, 7]))
print(solution1([5, 0, 2, 7]))
