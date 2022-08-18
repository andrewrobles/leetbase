# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        queue = [root]
        visited = {root}
        while queue:
            curr = queue.pop(0)
            if curr.val == val:
                return curr
            for child in [curr.left, curr.right]:
                if child is not None and child not in visited:
                    visited.add(child)
                    queue.append(child)
        return None
        
        
        