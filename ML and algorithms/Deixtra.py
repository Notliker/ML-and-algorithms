N, S, F = map(int, input().split())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

dist, visited = [float('inf')] * N, [0] * N
dist[S - 1] = 0


def graph(s, f, distance):
    visited[s] = 1
    distance = [distance[s] + arr[s][x] if arr[s][x] > 0 and distance[s] + arr[s][x] < distance[x] else distance[x] for x in range(N)]
    nodes = sorted([[distance[x], x] for x in range(N) if not visited[x]], key=lambda x: x[0])
    return distance[f] if s == f else graph(nodes[0][1], f, distance)


ans = graph(S - 1, F - 1, dist)
print(ans) if ans < float('inf') else print(-1)