def solution(board, moves):
    basket = []
    n = len(board)
    answer = 0

    for m in moves:
        for i in range(n):
            if board[i][m-1] != 0:
                basket.append(board[i][m-1])
                board[i][m-1] = 0
                break
        try:
            if basket[-1] == basket[-2]:
                basket = basket[:-2]
                answer += 2
        except:
            continue
    return answer