def main():
    v, edges = parse()
    students = {}
    for i in range(v):
        students[i + 1] = []

    for s1, s2 in edges:
        students[s1].append(s2)
        students[s2].append(s1)

    vertexes = []
    visited = [False for _ in range(v + 1)]
    color = [False for _ in range(v + 1)]
    # Проходим по каждой вершине
    for key in students:
        if not visited[key]:
            vertexes.append(key)
        # DFS-method проверки графа на двудольность при помощи перекрашивания посещенных вершин:
        while vertexes:
            curr_v = vertexes.pop()
            visited[curr_v] = True
            for v in students[curr_v]:
                if not visited[v]:
                    color[v] = not color[curr_v]
                    vertexes.append(v)
                elif color[curr_v] == color[v]:
                    return 'NO'

    return "YES"


def parse():
    n, m = [int(_) for _ in input().split()]
    nums = [[int(_) for _ in input().split()] for i in range(m)]
    return n, nums


if __name__ == '__main__':
    print(main())
