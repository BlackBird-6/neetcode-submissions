# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    
        def dfs(node, path, target):
            if node == target:
                return path
            
            res = None
            if node.left:
                res = dfs(node.left, path + [node.left], target)
            if not res and node.right:
                res = dfs(node.right, path + [node.right], target)
            return res

        path_p = dfs(root, [root], p)
        path_q = dfs(root, [root], q)
        # print(path_p, path_q)
        
        res = None
        for i in range(min(len(path_p), len(path_q))):
            if path_p[i] == path_q[i]:
                res = path_p[i]
        return res