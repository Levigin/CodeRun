def main():
    n = int(input())
    carnations = [int(_) for _ in input().split()]
    carnations.sort()
    print(f'{carnations = }')

    d = [0] * n
    d[1] = carnations[1] - carnations[0]
    if n > 2:
        d[2] = carnations[2] - carnations[0]
        for i in range(3, n):
            d[i] = min(d[i - 2], d[i - 1]) + carnations[i] - carnations[i - 1]

    print(f'{d = }')
    print(d[n - 1])


if __name__ == '__main__':
    print(main())
