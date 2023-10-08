def main():
    v, edges = parse()
    graph = {}
    for i in range(v):
        graph[i + 1] = set()

    for v1, v2 in edges:
        graph[v1].add(v2)
        graph[v2].add(v1)

    vertexes = [1]
    visited = set()
    while vertexes:
        cur_v = vertexes.pop()
        visited.add(cur_v)

        for v in graph[cur_v] - visited:
            graph[cur_v].remove(v)
            graph[v].remove(cur_v)
            vertexes.append(v)

    print(len(visited))
    print(*sorted(visited))


def parse():
    v, e = [int(_) for _ in input().split()]
    return v, [(int(i) for i in input().split()) for _ in range(e)]


if __name__ == '__main__':
    main()

