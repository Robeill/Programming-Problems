A = set(input())
n = int(input())
Flag = True
for i in range(n):
    n = set(input().split())
    if n not in A:
        Flag = False
print(Flag)