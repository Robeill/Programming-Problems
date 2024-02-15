n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
for i in range(0,n):
    rank = arr[k-1]
    if arr[i] >= rank and arr[i] != 0:
        count += 1
print(count)
