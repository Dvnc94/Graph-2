"""
TC = O(V + E)
SC = O(V + E)
"""


class Solution:
    def __init__(self):
        self.time = 0

    def getGraph(self, n, connections):
        adjList = []

        for i in range(n):
            adjList.append([])

        for edge in connections:
            _from = edge[0]
            to = edge[1]
            adjList[_from].append(to)
            adjList[to].append(_from)
        return adjList

    def dfs(self, graph, discovery, lowest, v, parent, rtnData):
        if discovery[v] != -1: return

        discovery[v] = self.time
        lowest[v] = self.time
        self.time += 1

        for child_v in graph[v]:
            if child_v == parent: continue

            if discovery[child_v] == -1:
                self.dfs(graph, discovery, lowest, child_v, v, rtnData)

                if lowest[child_v] > discovery[v]:
                    rtnData.append([child_v, v])
                lowest[v] = min(lowest[v], lowest[child_v])
            else:
                lowest[v] = min(lowest[v], lowest[child_v])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        if n is None or len(connections) == 0: return []

        rtnData = []

        discovery = [-1] * n
        lowest = [-1] * n

        graph = self.getGraph(n, connections)
 
        self.dfs(graph, discovery, lowest, 0, -1, rtnData)

        return rtnData