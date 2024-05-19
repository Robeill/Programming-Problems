n = int(input())
nums = list(map(int , input().split()))
res = [0] * n
x = 0  
for i in range(n):
    res[i] = nums[i] + x
    x = max(x, res[i])  # Update x for the next iteration
print(*res)
