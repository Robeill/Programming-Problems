n, m = map(int, input().split())
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
res = ""
r = 0
for l in range(m):
    while r < n and num2[l] > num1[r]:
        r += 1
    res += str(r) + " "
while len(res) < m:
    res += str(r) + " "
print(res)
