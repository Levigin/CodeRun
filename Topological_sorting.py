import sys

sys.setrecursionlimit(100_001)


def parse():
    n, m = [int(_) for _ in input().split()]
    nums = [[int(_) for _ in input().split()] for i in range(m)]
    return n, nums


def main():
    n, edges = parse()
    graph = {}
    for i in range(n):
        graph[i + 1] = []

    for v1, v2 in edges:
        graph[v1].append(v2)

    visited = [False for _ in range(n + 1)]
    rec_stack = [False for _ in range(n + 1)]
    result = []
    for v in graph:
        if not visited[v]:
            if dfs(graph, v, visited, result, rec_stack) == -1:
                print(f'{rec_stack = }')
                return [-1]

    return reversed(result)


def dfs(graph: dict[int, list], v: int, visited: list[bool], result: list[int], rec_stack: list[int]):
    # Топологическая сортировка с проверкой на цикличность
    visited[v] = True
    # Текущий стэк в котором проверяется цикличность ориентированного графа
    rec_stack[v] = True
    for v_ in graph[v]:
        if not visited[v_]:
            if dfs(graph, v_, visited, result, rec_stack) == -1:
                return -1
        elif rec_stack[v_]:
            return -1
    # необходимо добавлять в результат, что бы топологически отсортировать граф
    result.append(v)
    # rec_stack[v] = False


if __name__ == '__main__':
    print(*main())
