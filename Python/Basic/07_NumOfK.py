def solution(array, commands):
    answer = []
    arr = []

    for i in range(len(commands)):
        for j in range(commands[i][0] - 1, commands[i][1], 1):
            arr.append(array[j])
        arr.sort()
        answer.append(arr[commands[i][2] - 1])
        del arr[:]

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
