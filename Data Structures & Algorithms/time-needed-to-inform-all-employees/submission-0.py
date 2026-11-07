class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:     
        g = defaultdict(list)
        res = 0
        for i in range(len(manager)):
            g[manager[i]].append((informTime[manager[i]], i))

        seen = set([headID])
        to_visit = [(0, headID)]
        while to_visit:
            curr_time, curr = heapq.heappop(to_visit)
            seen.add(curr)
            # print(curr, curr_time)
            res = max(res, curr_time)
            for add_time, adj in g[curr]:
                # print(curr, g[curr], curr_time, add_time)
                if adj in seen:
                    continue
                heapq.heappush(to_visit, (curr_time + add_time, adj))
                
            if len(seen) == n:
                return res
        