import sys
from collections import deque

t = int(input())
# 위상 정렬 알고리즘
for _ in range(t):
    n, k = map(int, sys.stdin.readline().rstrip().split())  # 건물 개수와 건설 규칙 개수
    d = list(map(int, sys.stdin.readline().rstrip().split()))  # 각 건물 마다 건설하는데 걸리는 시간
    inDgree = [0 for _ in range(n + 1)]  # 위상 정렬 -> 차수
    dt = [0 for _ in range(n + 1)]  # 최종적으로 그 건물까지 걸리는 시간
    graph = [[] for _ in range(n + 1)]  # 건설 규칙 삽입
    queue = deque()  # 큐

    for i in range(k):  ##건설 규칙 넣고 각 건물마다 차수 입력
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        inDgree[b] += 1

    w = int(sys.stdin.readline().rstrip())

    for i in range(1, n + 1):  # 차수가 0인 건물을 큐에 넣기 (처음 시작 노드)
        if inDgree[i] == 0:
            queue.append(i)
            dt[i] = d[i - 1]  # 시작 지점은 차수가 0이기 때문에 건설시간이 그대로이다.

    while queue:  # q가 빌떄까지 진행
        a = queue.popleft()  # 큐에서 하나 pop
        for i in graph[a]:  # pop한 노드와 연결된 노드들 확인
            inDgree[i] -= 1  # 각각 차수 1 줄이기
            dt[i] = max(
                dt[a] + d[i - 1], dt[i]
            )  # 기존의 자신의 최종 건설시간과 (자신의 건설시간 + 자기와 연결된 노드의 시간) 중에 큰 것을 골라야 한다.
            if inDgree[i] == 0:  # 차수가 0이면
                queue.append(i)  # 큐에 넣는다.

    print(dt[w])
