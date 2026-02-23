def distribute (a, b, c, n):
    if n != 0:  
        max_coins = max(a, max(b,c))
        n -= (max_coins - a) + (max_coins - b) + (max_coins - c)
        if n % 3 == 0 and n >= 0:
            print("YES")
        else:
            print("NO")
    else:
        print("YES" if a == b == c else "NO")

t= int(input())
for i in range(t):
    a, b, c, n = map(int, input().split())
    distribute(a,b,c,n)
