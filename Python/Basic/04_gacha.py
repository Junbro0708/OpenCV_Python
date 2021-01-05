def solution(board, moves):
    answer = 0
    basket = []

    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i] - 1] == 0:
                pass
            else:
                basket.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1] = 0
                break

    for i in range(len(moves)):
        for k in range(0, len(basket) - 1, 1):
            if basket[k] == basket[k + 1]:
                basket.pop(k)
                basket.pop(k)  # k가 두 번인 이유는 k를 뺀다음 또 k 자리가 k+1이기 때문
                answer += 2
                break

    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
