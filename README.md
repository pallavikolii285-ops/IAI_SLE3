# Empirical Performance Profiling Engine: BFS vs DFS

## 1. Aim and Objectives

**Aim:** To document the architecture of a Python-based profiling program that compares Breadth-First Search (BFS) and Depth-First Search (DFS) using a four-level C4-style architectural perspective.

**Objectives:**
- Show the system boundary and its interaction with the evaluator.
- Describe the main containers and how the benchmark is organized.
- Explain the internal traversal and measurement components.
- Relate the architecture to the Python implementation in `dfs_vs_bfs.py`.

## 2. System Overview

This project compares two uninformed graph-search algorithms:

- **Breadth-First Search (BFS):** explores nodes using a FIFO queue implemented with `collections.deque`.
- **Depth-First Search (DFS):** explores nodes using a LIFO stack implemented with a Python list.

The program uses a predefined directed graph, a start node, and a goal node. It records the number of expanded nodes and elapsed time for repeated executions, then prints average measurements for comparison.

### Benchmark configuration in the current source code

| Setting | Value |
|---|---|
| Graph | Predefined adjacency dictionary |
| Number of nodes | 20 (nodes `0`–`19`) |
| Start node | `0` |
| Goal node | `19` |
| Runs | `3` |
| Repetitions per run | `1000` |
| Timing | `timeit.default_timer()` |
| Reported metrics | Elapsed time in milliseconds and nodes expanded |

> **Note:** These values reflect the current `dfs_vs_bfs.py` source. They are not the 1,200-node configuration described in some reference material.

## 3. C4 Architectural Model

### Level 1: System Context

The system context view identifies the evaluator and the profiling program.

- **Person:** Student, evaluator, or reviewer who runs and inspects the benchmark.
- **System:** BFS vs DFS performance profiling program.
- **Inputs:** Graph configuration and the `START`, `GOAL`, `RUNS`, and `REPEAT` constants defined in the source.
- **Outputs:** Per-run timings, node-expansion counts, averages, and a final comparison table.

![Level 1: System Context Diagram](C:\Users\HP\Downloads\C1.drawio.png)

### Level 2: Container

The container view describes the major responsibilities inside the program:

1. **Graph data:** The adjacency dictionary stores each node and its outgoing neighbours.
2. **Search execution:** The BFS and DFS functions traverse the graph and count expanded nodes.
3. **Benchmark loop:** The program repeats each search `REPEAT` times in each run and measures elapsed time.
4. **Result aggregation and reporting:** Lists collect timing and node-count measurements; averages and a final comparison table are printed.

![Level 2: Container Diagram](C:\Users\HP\Downloads\C2.drawio.png)

### Level 3: Component

The component view focuses on the main logical parts involved in running and measuring a search:

- **BFS traversal:** Initializes a deque with the start node, removes the next node with `popleft()`, tracks visited nodes, and checks the goal.
- **DFS traversal:** Initializes a list-based stack, removes the top node with `pop()`, tracks visited nodes, and checks the goal.
- **Node-expansion counter:** Increments when a node is visited for the first time.
- **Timing and repetition controller:** Runs each algorithm repeatedly and records elapsed time.
- **Summary/reporting logic:** Calculates average elapsed time and average expanded-node counts for BFS and DFS.

![Level 3: Component Diagram](C:\Users\HP\Downloads\C3.drawio.png)


### Level 4: Code-Level Mapping

The current repository contains the Python source file `dfs_vs_bfs.py`. Its key implementation elements are:

| Code element | Responsibility |
|---|---|
| `graph` | Stores the predefined graph as an adjacency dictionary |
| `START`, `GOAL` | Set the initial node and target node |
| `RUNS`, `REPEAT` | Configure the benchmark loops |
| `bfs()` | Runs queue-based breadth-first traversal and returns the number of expanded nodes |
| `dfs()` | Runs stack-based depth-first traversal and returns the number of expanded nodes |
| `timeit.default_timer()` | Measures the elapsed time around each group of repeated searches |
| Average calculations | Compute mean timings and mean node counts |
| Final comparison output | Displays BFS and DFS metrics in a formatted table |

The DFS implementation iterates over `reversed(graph[current])` when adding neighbours to the stack. This controls the order in which the stack explores neighbours.

**Diagram availability:** The repository currently includes Context, Container, and Component diagram images. A separate Level 4 code diagram is not listed in the current repository file list; the code mapping above documents the implementation in text.

## 4. Architectural Design Decisions

- **Separate traversal functions:** BFS and DFS are implemented independently, making their data structures and traversal behaviour easier to compare.
- **Visited set:** Both functions use a set to avoid expanding the same node more than once.
- **Repeated measurements:** Each algorithm is run multiple times per benchmark run, and the program calculates average measurements.
- **Same graph and endpoints:** Both algorithms use the same graph, start node, and goal node so their results can be compared under the same setup.
- **Neighbour-order control in DFS:** Reversing the neighbour sequence before pushing it onto the stack gives deterministic stack traversal order for the current adjacency lists.

## 5. Repository File Structure

```text
IAI_SLE3/
├── Context_Diagram.png       # System context view
├── Container_Diagram.png     # Container architecture view
├── Component_Diagram.png     # Component-level view
├── dfs_vs_bfs.py             # BFS/DFS benchmark implementation
└── README.md                 # Project and architecture documentation
```

## 6. Requirements

- Python 3
- No third-party packages are required; the program uses Python standard-library modules (`collections` and `timeit`).

## 7. How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/pallavikolii285-ops/IAI_SLE3.git
   ```

2. Open the project directory:

   ```bash
   cd IAI_SLE3
   ```

3. Run the benchmark:

   ```bash
   python dfs_vs_bfs.py
   ```

The program prints the benchmark configuration, individual BFS and DFS run measurements, and a final comparison containing average time, average nodes expanded, and goal-found status.

## 8. Expected Output

Exact timings depend on the computer and operating-system workload, so they can differ between runs. The script reports:
- elapsed time in milliseconds for each run;
- node counts returned by BFS and DFS;
- average elapsed time for each algorithm;
- average expanded-node count for each algorithm; and
- the goal-found status displayed by the program.

## 9. Conclusion

This project provides a small, reproducible benchmark for observing BFS and DFS on the same predefined graph. Its C4-style diagrams describe the system context, containers, and components, while the code-level mapping connects those views to the actual Python implementation. Timing results should be interpreted as measurements from the current environment rather than universal performance guarantees.
