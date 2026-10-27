from typing import List

def floyd_warshall(graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def optimal_bst(keys: List[int], freq: List[int]) -> int:
    n = len(keys)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = freq[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            total = sum(freq[i:j + 1])

            for r in range(i, j + 1):
                left = dp[i][r - 1] if r > i else 0
                right = dp[r + 1][j] if r < j else 0
                cost = left + right + total
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1] if n > 0 else 0


graph = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]

print(floyd_warshall(graph))

keys = [10, 20, 30]
freq = [34, 8, 50]

print("optimal_bst(keys, freq):", optimal_bst(keys, freq))