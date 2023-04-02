n = int(input())

endNumList = [
    [10],
    [1],
    [2, 4, 8, 6],
    [3, 9, 7, 1],
    [4, 6],
    [5],
    [6],
    [7, 9, 3, 1],
    [8, 4, 2, 6],
    [9, 1],
]


def FindEndNum(a, b):
    a1 = a % 10
    b1 = b % len(endNumList[a1])
    EndNum = endNumList[a1][b1 - 1]
    return EndNum


for _ in range(n):
    a, b = map(int, input().split())
    print(FindEndNum(a, b))
