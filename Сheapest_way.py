def main():
    n, m = [int(i) for i in input().strip().split()]
    arrays = [[int(_) for _ in input().strip().split()] for _ in range(n)]
    print(f'{arrays = }')
    dp = [[1001] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j == 1:
                dp[i][j] = arrays[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + arrays[i - 1][j - 1]

    for i in range(n + 1):
        for j in range(m + 1):
            print(dp[i][j], end=' ')
        print()

    return dp[n][m]


if __name__ == '__main__':
    print(f'Ans: {main()}')
