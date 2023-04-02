n = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = [(x, y)]
    matrix[x][y] = 0

    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if matrix[nx][ny] == 1:
                    queue.append((nx, ny))
                    matrix[nx][ny] = 0


for _ in range(n):
    m, n, k = map(int, input().split())
    matrix = [[0] * n for _ in range(m)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        matrix[x][y] = 1

    for a in range(m):
        for b in range(n):
            if matrix[a][b] == 1:
                bfs(a, b)
                cnt += 1
    print(cnt)
