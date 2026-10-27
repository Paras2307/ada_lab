from typing import List

class TSPSolver:
    def solve_tsp(self, dist_matrix: List[List[int]]) -> int:
        n = len(dist_matrix)
        visited = [False] * n
        visited[0] = True

        def backtrack(city, count, cost):
            if count == n:
                return cost + dist_matrix[city][0]

            ans = float('inf')

            for next_city in range(n):
                if not visited[next_city]:
                    visited[next_city] = True

                    ans = min(ans, backtrack(
                        next_city, count + 1,
                        cost + dist_matrix[city][next_city]
                    ))

                    visited[next_city] = False

            return ans

        return backtrack(0, 1, 0)


dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

solver = TSPSolver()
print("solver.solve_tsp(dist_matrix):", solver.solve_tsp(dist_matrix))