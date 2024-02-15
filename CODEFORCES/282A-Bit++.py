n = int(input())
x = 0
for i in range(0,n):
    op = input()
    #count the character and change the value of x accordingly
    if op.count('++') == 1:
        x += 1
    if op.count('--') == 1:
        x -= 1
print(x)
    