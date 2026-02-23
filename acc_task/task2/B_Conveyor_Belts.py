def Conveyor  (n, x1, y1, x2, y2):
    point1 = max(n-x1+1, max(n-y1+1, max(x1,y1)))
    point2 = max(n-x2+1, max(n-y2+1, max(x2,y2)))
    print(abs(point1-point2))

t= int(input())
for i in range(t):
    n, x1, y1, x2, y2 = map(int, input().split())
    Conveyor (n, x1, y1, x2, y2)
