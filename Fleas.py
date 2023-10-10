from collections import deque


def parse():
    n, m, s, t, q = [int(_) for _ in input().split()]
    coords = [[int(_) for _ in input().split()] for i in range(q)]
    return n, m, s, t, q, coords


def main():
    n, m, s, t, q, coords = parse()
    vertexes = deque()
    vertexes.append([s - 1, t - 1, 0])
    # Количество прыжков необходимых для достижения кормушки:
    jumps = 0
    # Использование множества, лучше чем список для добавления посещенных вершин:
    visited = {(s - 1, t - 1)}
    # Используем словарь для хранения количество необходимых прыжков с определенной координаты
    full = {(s, t): 0}
    # bfs:
    while vertexes:
        # print(f'{vertexes = }')
        # print(f'{visited = }')
        v_ = vertexes.popleft()

        for v in get_vert(v_[0], v_[1], n, m) - visited:
            visited.add(v)
            vertexes.append([v[0], v[1], v_[2] + 1])
            full[(v[0] + 1, v[1] + 1)] = v_[2] + 1

    # print(f'{full = }')
    for coord in coords:
        if tuple(coord) not in full:
            return -1
        jumps += full[tuple(coord)]

    return jumps


def get_vert(y: int, x: int, n: int, m: int):
    # Координаты движения коня по доске
    steps = [(1, 2), (2, 1), (-1, -2), (-2, -1), (1, -2), (-1, 2), (2, -1), (-2, 1)]
    neighs = set()
    # Нахождение соседних вершин
    for step in steps:
        y_, x_ = step[0] + y, step[1] + x
        if 0 <= x_ < m and 0 <= y_ < n:
            neighs.add((y_, x_))

    return neighs


if __name__ == '__main__':
    print(f'{main()}')
