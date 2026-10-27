from typing import List

class GraphBacktracker:
    def __init__(self, graph: List[List[int]]):
        self.graph = graph
        self.n = len(graph)

    def graph_coloring(self, m: int) -> List[int]:
        colors = [0] * self.n

        def is_safe(v, color):
            for i in range(self.n):
                if self.graph[v][i] and colors[i] == color:
                    return False
            return True

        def backtrack(v):
            if v == self.n:
                return True

            for color in range(1, m + 1):
                if is_safe(v, color):
                    colors[v] = color

                    if backtrack(v + 1):
                        return True

                    colors[v] = 0

            return False

        if backtrack(0):
            return colors
        return []

    def hamiltonian_cycle(self) -> List[int]:
        path = [0] + [-1] * (self.n - 1)

        def is_safe(v, pos):
            if self.graph[path[pos - 1]][v] == 0:
                return False

            if v in path[:pos]:
                return False

            return True

        def backtrack(pos):
            if pos == self.n:
                return self.graph[path[pos - 1]][path[0]] != 0

            for v in range(1, self.n):
                if is_safe(v, pos):
                    path[pos] = v

                    if backtrack(pos + 1):
                        return True

                    path[pos] = -1

            return False

        if backtrack(1):
            return path + [path[0]]
        return []


graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

solver = GraphBacktracker(graph)

print("Graph Coloring:", solver.graph_coloring(3))
print("Hamiltonian Cycle:", solver.hamiltonian_cycle())