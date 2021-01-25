def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return "김서방은 {}에 있다".format(i)


def solution1(seoul):
    return "김서방은 {}에 있다".format(seoul.index("Kim"))


print(solution1(["Jane", "Kim"]))
