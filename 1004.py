def planet_num(n):
    for i in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        p_num = int(input())
        count = 0
        for j in range(p_num):
            cx, cy, cr = map(int, input().split())
            dis1 = (x1 - cx) ** 2 + (y1 - cy) ** 2
            dis2 = (x2 - cx) ** 2 + (y2 - cy) ** 2
            disr = cr**2

            if disr > dis1 and disr > dis2:
                pass
            elif disr > dis1:
                count += 1
            elif disr > dis2:
                count += 1
        print(count)


planet_num(int(input()))
