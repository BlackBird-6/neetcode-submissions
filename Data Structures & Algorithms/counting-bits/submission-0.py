class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        while len(res) < n+1:
            doubled_arr = []
            for i in range(len(res)):
                doubled_arr.append(res[i])
                doubled_arr.append(res[i]+1)
            res = doubled_arr
        return res[:n+1]

        # [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
        