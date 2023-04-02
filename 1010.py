import math

n = int(input())


def BridgeNum(n, m):
    num = math.comb(m, n)
    return num


for _ in range(n):
    a, b = map(int, input().split())
    print(BridgeNum(a, b))
