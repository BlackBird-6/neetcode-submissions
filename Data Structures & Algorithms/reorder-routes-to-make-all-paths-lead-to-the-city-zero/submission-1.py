from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        sys.setrecursionlimit(1000000)

        directed_edges = {(a, b) for a, b in connections}
        g = defaultdict(list)

        for a, b in connections:
            g[a].append(b)
            g[b].append(a)

        res = 0
        seen = set()
        def dfs(node):
            nonlocal res
            seen.add(node)
            for nei in g[node]:
                if nei in seen:
                    continue

                dfs(nei)
                if (nei, node) in directed_edges:
                    continue
                res += 1
        dfs(0)
        return res