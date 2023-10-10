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
    nodes = {start: None}
    visited = []
    length = len(matrix[0])
    flag = False
    while vertexes:
        curr_v = vertexes.popleft()
        visited.append(curr_v[0])

        if curr_v[0] == end - 1:
            flag = True
            path_len = curr_v[1]
            break

        for i in range(0, curr_v[0]):
            if matrix[i][curr_v[0]] == 1 and i not in visited:
                vertexes.append((i, curr_v[1] + 1))
                visited.append(i)
                nodes[i + 1] = curr_v[0] + 1
        for i in range(curr_v[0], length):
            if matrix[curr_v[0]][i] == 1 and i not in visited:
                vertexes.append((i, curr_v[1] + 1))
                visited.append(i)
                nodes[i + 1] = curr_v[0] + 1
    if flag:
        res = []
        i = end
        while i is not None:
            res.append(i)
            i = nodes[i]
        print(path_len)
        if path_len != 0:
            print(*res[::-1])
    else:
        print(-1)


if __name__ == '__main__':
    print(f'Ans: {main()}')
