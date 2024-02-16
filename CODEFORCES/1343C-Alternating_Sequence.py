def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0

t = int(input())
for k in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    total_sum = 0
    i = 0
    while i < n:
        cur = a[i]
        j = i + 1
        while j < n and sgn(a[i]) == sgn(a[j]):
            cur = max(cur, a[j])
            j += 1
        total_sum += cur
        i = j 
    print(total_sum)
