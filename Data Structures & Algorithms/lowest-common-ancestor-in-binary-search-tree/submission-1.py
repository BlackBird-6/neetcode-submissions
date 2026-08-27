# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    
        def dfs(node, path, target):
            if node == None:
                return None
            
            path.append(node)

            if node == target:
                return path

            res = dfs(node.left, path, target) or dfs(node.right, path, target)

            if res:
                return path
            
            path.pop()

        path_p = dfs(root, [], p)
        path_q = dfs(root, [], q)
        print(path_p, path_q)
        
        res = None
        for i in range(min(len(path_p), len(path_q))):
            if path_p[i] == path_q[i]:
                res = path_p[i]
        return res