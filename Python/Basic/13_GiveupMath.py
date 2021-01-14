def solution(answers):
    answer = []

    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    grade = [0, 0, 0]
    maxScore = 0

    for i in range(len(answers)):
        if arr1[i] == answers[i]:
            grade[0] += 1
        if arr2[i] == answers[i]:
            grade[1] += 1
        if arr3[i] == answers[i]:
            grade[2] += 1

    for i in range(3):
        if maxScore < grade[i] != 0:
            answer.insert(0, i + 1)
            maxScore = grade[i]
        elif maxScore >= grade[i] != 0:
            answer.append(i + 1)

    return answer


print(solution([1, 2, 3, 4, 5]))
