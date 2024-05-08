from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    s = input().rstrip()
    d[s].append(i+1)
for j in range(m):
    s = input().rstrip()
    if s in d:
        print(' '.join(map(str,d[s])))
    else:
        print('-1')