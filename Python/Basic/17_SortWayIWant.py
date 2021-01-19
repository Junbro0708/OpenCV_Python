def solution(strings, n):
    answer = []
    result = []

    for i in range(len(strings)):
        answer.append(strings[i][n])

    answer.sort()

    for i in range(len(answer)):
        for j in range(len(strings)):
            if answer[i] in strings[j][n]:
                result.append(strings[j])
                strings.remove(strings[j])
                break

    return result


print(solution(["abcd", "abce", "cdx"], 2))
