def main():
    n, m = [int(_) for _ in input().split()]
    arrays = [[int(_) for _ in input().split()] for i in range(n)]
    dp = [[-1] * (m + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j == 1:
                dp[i][j] = arrays[0][0]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + arrays[i - 1][j - 1]

    for i in range(n + 1):
        for j in range(m + 1):
            print(dp[i][j], end=' ')
        print()

    x = m
    y = n
    res = []
    while True:
        if y == x == 1:
            break
        if dp[y - 1][x] > dp[y][x - 1]:
            res.append('D')
            y -= 1
        else:
            res.append('R')
            x -= 1

    res.reverse()
    print(f'{dp[-1][-1]}')
    print(f'{(" ").join(res)}')


if __name__ == '__main__':
    main()
