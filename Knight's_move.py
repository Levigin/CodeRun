def main():
    n, m = [int(_) for _ in input().split()]

    board = [[-1] * m for _ in range(n)]
    board[0][0] = 1

    def rec(i: int, j: int):
        if 0 <= i < n and 0 <= j < m:
            if board[i][j] == -1:
                board[i][j] = rec(i - 2, j - 1) + rec(i - 1, j - 2)
        else:
            return 0
        return board[i][j]

    print(rec(n - 1, m - 1))


def main_():
    n, m = [int(_) for _ in input().split()]

    board = [[0] * (m + 1) for _ in range(n + 1)]
    board[1][1] = 1

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            board[i][j] = board[i - 2][j - 1] + board[i - 1][j - 2]

    for i in range(n + 1):
        for j in range(m + 1):
            print(board[i][j], end=' ')
        print()

    print(f'{board[n][m]}')


if __name__ == '__main__':
    main_()
