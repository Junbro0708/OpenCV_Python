def solution(s):
    answer = ""
    char = sorted(s)
    for i in range(len(char) - 1, -1, -1):
        answer += char[i]
    return answer


print(solution("Zbcdefg"))
