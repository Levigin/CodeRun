import random
import time


start: int


def main():
    global start
    v, edges = parse()
    graph = {}
    for i in range(v):
        graph[i + 1] = set()

    for v1, v2 in edges:
        graph[v1].add(v2)
        graph[v2].add(v1)

    res = []
    vertexes = set()
    # start = time.time_ns()
    visited = set()

    for key in graph:
        temp = []
        if key not in visited:
            vertexes.add(key)
            while vertexes:
                cur_v = vertexes.pop()
                visited.add(cur_v)
                temp.append(cur_v)
                for v in graph[cur_v] - visited:
                    graph[cur_v].remove(v)
                    graph[v].remove(cur_v)
                    vertexes.add(v)
            res.append(temp)
    # finish = time.time_ns()
    # print(f'Time: {(finish - start) // 10 ** 6} mls')
    print(f'{len(res)}')
    for i in res:
        print(f'{len(i)}')
        print(*i)


def parse():
    v, e = [int(_) for _ in input().split()]
    return v, [(int(i) for i in input().split()) for _ in range(e)]


def dfs(graph: dict[int], start: int, visited: set[int]):
    vertexes = [start]
    while vertexes:
        cur_v = vertexes.pop()
        visited.add(cur_v)

        for v in graph[cur_v] - visited:
            graph[cur_v].remove(v)
            graph[v].remove(cur_v)
            vertexes.append(v)
    return visited


if __name__ == '__main__':
    main()


