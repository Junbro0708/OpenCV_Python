def solution(s):
    if len(s) % 2 == 0:
        answer = s[int(len(s) / 2) - 1] + s[int(len(s) / 2)]
    else:
        answer = s[int(len(s) / 2)]
    return answer


print(solution("Hello"))

