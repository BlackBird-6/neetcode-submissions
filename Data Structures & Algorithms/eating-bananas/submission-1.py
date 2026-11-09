class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def trial(k):
            res = 0
            for p in piles:
                res += math.ceil(p/k)
            return res
        
        low = 1
        high = 1000000000
        
        while low < high:
            print(low, high)
            par = (low+high)//2

            if trial(par) > h:
                low = par+1
            if trial(par) <= h:
                high = par
        return high
        


        