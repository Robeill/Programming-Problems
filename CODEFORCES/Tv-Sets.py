n , m = map(int , input().split())
nums = list(map(int , input().split()))
nums.sort()
res = 0
for i in range(min(m,n)):
    if nums[i] < 0:
        res += abs(nums[i])
    else:
        break
print(res)