n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
i = 0
sum_val = 0
for _ in range(k):
    while i < len(arr) and arr[i] - sum_val == 0:
        i += 1
    if i < len(arr) and arr[i] - sum_val > 0:
        print(arr[i] - sum_val)
        sum_val = arr[i]
    else:
        print(0)