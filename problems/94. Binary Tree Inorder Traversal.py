# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        return self.dfs(root)

    def dfs(self,root):
        pointer = root 
        stack = []
        output = []
        if not pointer:
            return []

        if pointer.right:
            #stack.insert(0,pointer.right.val)
            stack = stack + self.dfs(pointer.right)

        stack.insert(0,root.val)

        if pointer.left:
            #stack.insert(0, pointer.left.val)
            stack = self.dfs(pointer.left) + stack
        
        
    
        return stack