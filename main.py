# поиск в глубину
def dfs(graph, v, visited, spanning_tree):
    visited[v] = True
    
    for neighbor in graph[v]:
        if not visited[neighbor]:
            spanning_tree.append((v, neighbor)) 
            dfs(graph, neighbor, visited, spanning_tree)

# построение глубинного остовного дерева
def build_spanning_tree(graph):
    n = len(graph)
    spanning_tree = [] # ребра остовного дерева
    visited = [False] * n

    # Старт c 0 вершины
    for v in range(n):
        if not visited[v]:
            dfs(graph, v, visited, spanning_tree)
            
    return spanning_tree


if __name__ == "__main__":
    # Обычный граф, без циклов
    graph1 = {
        0: [1],
        1: [0, 2],
        2: [1, 3],
        3: [2]
    }
    spanning_tree1 = build_spanning_tree(graph1)
    expected_spanning_tree1 = [(0, 1), (1, 2), (2, 3)]
    assert sorted(spanning_tree1) == sorted(expected_spanning_tree1), f"Ошибка: {spanning_tree1}"

     # Граф с циклами
    graph2 = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2, 4],
        4: [3]

    }
    spanning_tree2 = build_spanning_tree(graph2)
    expected_spanning_tree2 = [(0, 1), (1, 2), (2, 3), (3, 4)]
    assert set(spanning_tree2) == set(expected_spanning_tree2), f"Ошибка: {spanning_tree2}"

    # Граф с несколькими компонентами связности
    graph3 = {
        0: [1],
        1: [0, 2],
        2: [1],
        3: [4],
        4: [3]
    }
    spanning_tree3 = build_spanning_tree(graph3)
    expected_spanning_tree3 = [(0, 1), (1, 2), (3, 4)]
    assert sorted(spanning_tree3) == sorted(expected_spanning_tree3), f"Ошибка: {spanning_tree3}"

    # Изолированные вершины
    graph4 = {
        0: [1],
        1: [0],
        2: [],
        3: [],
        4: []
    }
    spanning_tree4 = build_spanning_tree(graph4)
    expected_spanning_tree4 = [(0, 1)]  # Изолированные вершины не входят в остовное дерево
    assert spanning_tree4 == expected_spanning_tree4, f"Ошибка: {spanning_tree4}"

    # Полный граф
    graph5 = {
        0: [1, 2, 3, 4],
        1: [0, 2, 3, 4],
        2: [0, 1, 3, 4],
        3: [0, 1, 2, 4],
        4: [0, 1, 2, 3]
    }
    spanning_tree5 = build_spanning_tree(graph5)
    expected_spanning_tree5 = [(0, 1), (1, 2), (2, 3), (3, 4)]
    assert set(spanning_tree5) == set(expected_spanning_tree5), f"Ошибка: {spanning_tree5}"

    print("Done!")
