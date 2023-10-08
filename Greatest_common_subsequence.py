def main():
    n = int(input())
    arr1 = [int(i) for i in input().split()]
    m = int(input())
    arr2 = [int(i) for i in input().split()]

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i, a1 in enumerate(arr1):
        for j, a2 in enumerate(arr2):
            if a1 == a2:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    for i in range(n + 1):
        for j in range(m + 1):
            print(dp[i][j], end=' ')

        print(dp[n][m])

    LCS = []
    x, y = len(arr1) - 1, len(arr2) - 1
    while x >= 0 and y >= 0:
        print(f'{x = }, {y = }')
        if arr1[x] == arr2[y]:
            LCS.append(arr1[x])
            x, y = x - 1, y - 1
        elif dp[x - 1][y] > dp[x][y - 1]:
            x -= 1
        else:
            y -= 1
    LCS.reverse()
    return ' '.join(list(map(str, LCS)))


if __name__ == '__main__':
    print(main())