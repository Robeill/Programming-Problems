class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for neighbor in visit[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)
        
        visit = {}
        n = len(isConnected)
        for i in range(n):
            check = []
            for j in range(n):
                if isConnected[i][j] == 1:
                    check.append(j)
            visit[i] = check
        
        visited = [False] * n
        num_provinces = 0
        for i in range(n):
            if not visited[i]:
                num_provinces += 1
                visited[i] = True
                dfs(i)
        return num_provinces
