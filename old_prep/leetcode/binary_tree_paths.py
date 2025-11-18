# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []

        def choose(node, path):
            if not node:
                return
            
            if not node.left and not node.right:
                path = path + str(node.val)
                self.res.append(path)
                return
            
            path = path + str(node.val) + "->"
            choose(node.left,path)
            choose(node.right,path)

        choose(root,"")
        return self.res