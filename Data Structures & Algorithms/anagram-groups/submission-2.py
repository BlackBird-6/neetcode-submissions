class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def encodeLetters(s):
            res = [0]*26
            for c in s:
                res[ord(c) - ord('a')] += 1
            return tuple(res)
        
        groups = defaultdict(list)
        for s in strs:
            groups[encodeLetters(s)].append(s)
        return list(groups.values())