from collections import deque


def parse():
    vertexes = int(input())
    matrix = [[int(_) for _ in input().split()] for i in range(vertexes)]
    start, end = [int(_) for _ in input().split()]
    return matrix, start, end


def main():
    matrix, start, end = parse()
    vertexes = deque()
    vertexes.append((start - 1, 0))
    visited = []
    length = len(matrix[0])
    while vertexes:
        curr_v = vertexes.popleft()
        visited.append(curr_v[0])

        if curr_v[0] == end - 1:
            return curr_v[1]

        for i in range(0, curr_v[0]):
            if matrix[i][curr_v[0]] == 1 and i not in visited:
                vertexes.append((i, curr_v[1] + 1))
        for i in range(curr_v[0], length):
            if matrix[curr_v[0]][i] == 1 and i not in visited:
                vertexes.append((i, curr_v[1] + 1))

    return -1


if __name__ == '__main__':
    print(f'Ans: {main()}')
