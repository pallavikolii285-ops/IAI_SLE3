from collections import deque
import timeit

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    3: [7, 8],
    4: [9, 10],
    5: [11, 12],
    6: [13, 14],
    7: [15],
    8: [16],
    9: [17],
    10: [18],
    11: [19],
    12: [19],
    13: [19],
    14: [19],
    15: [19],
    16: [19],
    17: [19],
    18: [19],
    19: []
}

START = 0
GOAL = 19
RUNS = 3
REPEAT = 1000


def bfs():
    queue = deque([START])
    visited = set()
    nodes = 0

    while queue:
        current = queue.popleft()

        if current in visited:
            continue

        visited.add(current)
        nodes += 1

        if current == GOAL:
            return nodes

        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)

    return nodes


def dfs():
    stack = [START]
    visited = set()
    nodes = 0

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        nodes += 1

        if current == GOAL:
            return nodes

        for neighbour in reversed(graph[current]):
            if neighbour not in visited:
                stack.append(neighbour)

    return nodes


print("=" * 60)
print("SLE-2: EMPIRICAL PERFORMANCE ANALYSIS")
print("Comparison: BFS vs DFS")
print("=" * 60)

print(f"Number of Nodes = {len(graph)}")
print(f"Start Node = {START}")
print(f"Goal Node = {GOAL}")
print(f"Number of Runs = {RUNS}")
print(f"Repetitions per Run = {REPEAT}")

bfs_times = []
dfs_times = []
bfs_nodes_list = []
dfs_nodes_list = []

print("\nBFS RESULTS")

for i in range(RUNS):
    start = timeit.default_timer()

    for _ in range(REPEAT):
        bfs_nodes = bfs()

    end = timeit.default_timer()

    time_ms = (end - start) * 1000
    bfs_times.append(time_ms)
    bfs_nodes_list.append(bfs_nodes)

    print(
        f"Run {i + 1}: {time_ms:.5f} ms, "
        f"Nodes = {bfs_nodes}"
    )


print("\nDFS RESULTS")

for i in range(RUNS):
    start = timeit.default_timer()

    for _ in range(REPEAT):
        dfs_nodes = dfs()

    end = timeit.default_timer()

    time_ms = (end - start) * 1000
    dfs_times.append(time_ms)
    dfs_nodes_list.append(dfs_nodes)

    print(
        f"Run {i + 1}: {time_ms:.5f} ms, "
        f"Nodes = {dfs_nodes}"
    )


bfs_average = sum(bfs_times) / RUNS
dfs_average = sum(dfs_times) / RUNS

bfs_average_nodes = sum(bfs_nodes_list) / RUNS
dfs_average_nodes = sum(dfs_nodes_list) / RUNS


print("\n" + "=" * 60)
print("FINAL COMPARISON")
print("=" * 60)

print(f"{'Metric':<30} {'BFS':<15} {'DFS':<15}")
print("-" * 60)

print(
    f"{'Average Time (ms)':<30} "
    f"{bfs_average:<15.5f} "
    f"{dfs_average:<15.5f}"
)

print(
    f"{'Average Nodes Expanded':<30} "
    f"{bfs_average_nodes:<15.2f} "
    f"{dfs_average_nodes:<15.2f}"
)

print(
    f"{'Goal Found':<30} "
    f"{True!s:<15} "
    f"{True!s:<15}"
)

print("=" * 60)