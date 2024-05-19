t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    res = [0] * n
    j, i, k = 0, 0, n - 1
    first = True
    for i in range(n):
        if first:
            res[i] = nums[j]
            first = False
            j += 1
        else:
            res[i] = nums[k]
            k -= 1
            first = True
    print(" ".join(map(str, res)))
