a = [38, 21, 53, 62, 19]


def solution(list_l):
    a.sort()
    return list_l[len(list_l) - 1], list_l[0]


print(solution(a))

b = [i for i in range(1, 11) if i % 2 == 0]
print(b)

c = [[i, j] for i in range(1, 10)
     for j in range(1, 10)]
for i, j in c:
    print("{0} x {1} = {2}".format(i, j, i*j))

# slicing, enumerate, 리스트 내포

