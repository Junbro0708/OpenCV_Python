def solution(n, lost, reserve):
    stu = [i for i in range(1, n + 1)]
    for i in range(len(lost)):
        if lost[i] in stu:
            stu.remove(lost[i])

    for i in range(len(reserve)):
        if reserve[i] in lost:
            stu.append(reserve[i])
        elif reserve[i] - 1 in lost:
            stu.append(reserve[i] - 1)
        elif reserve[i] + 1 in lost:
            stu.append(reserve[i] + 1)

    return len(set(stu))


# def solution1(n, lost, reserve):
#     intersection = set(lost) & set(reserve)
#     lost_set = set(lost) - intersection
#     reserve_set = set(reserve) - intersection
#
#     return reserve_set
#
#
# print(solution1(5, [2, 4, 3], [3]))
