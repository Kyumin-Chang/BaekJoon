import math

def find_mem(x1,y1,r1,x2,y2,r2):
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
    r = r1+r2
    count = 0
    if distance == 0 and r1==r2:
        count = -1
    elif abs(r1-r2) == distance or r == distance:
        count = 1
    elif abs(r1-r2) < distance < r:
        count = 2
    else :
        count = 0
    print(count)

a = int(input())
n=0
while n < a:
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    find_mem(x1,y1,r1,x2,y2,r2)
    n+=1