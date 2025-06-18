"""
TC - O(n^2) 
SC - O(n)
"""
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        if graph is None or len(graph) == 0: return -1

        n = len(graph)
        colors = [-1 for i in range(n)]

        color = 0

        def dfs(graph, color, colors, i):
            if colors[i] != -1: return
            colors[i] = color
            for j in range(n):
                if graph[i][j] == 1:
                    dfs(graph, color, colors, j)

        for i in range(n):
            if colors[i] == -1:
                dfs(graph, color, colors, i)
                color += 1

        groups = [0 for i in range(color)]
        for i in range(n):
            index = colors[i]
            groups[index] += 1

        initinfected = [0 for i in range(color)]
        for i in range(len(initial)):
            index = initial[i]
            initinfected[colors[index]] += 1
        answer = float('inf')
        for i in range(len(initial)):
            colr = colors[initial[i]]
            if initinfected[colr] == 1:
                if answer == float('inf'):
                    answer = initial[i]
                elif(groups[colors[initial[i]]] > groups[colors[answer]]):
                    answer = initial[i]
                elif((groups[colors[initial[i]]] == groups[colors[answer]]) and initial[i] < answer):
                    answer = initial[i]
        if answer == float('inf'):
            minVal = float('inf')
            for i in range(len(initial)):
                minVal = min(minVal, initial[i])
            return minVal

        return answer  
