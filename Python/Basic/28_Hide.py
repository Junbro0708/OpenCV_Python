def solution(phone_number):
    for i in range(0, len(phone_number) - 4, 1):
        phone_number = list(phone_number)
        phone_number[i] = "*"
    return "".join(phone_number)


print(solution("02324123213"))
