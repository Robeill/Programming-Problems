t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    count = n
    v.sort()
    for i in range(1, n):
        if v[i] - v[i - 1] <= 1:
            count -= 1
    if count == 1:
        print("YES")
    else:
        print("NO")

