# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        # Find middle index
        middleIndex = len(nums) // 2
        
        # Make the middle element the root
        root = TreeNode(nums[middleIndex])
        
        # Left subtree has all values less than root
        root.left = self.sortedArrayToBST(nums[:middleIndex])
        
        # Right subtree has all values greater than root
        root.right = self.sortedArrayToBST(nums[middleIndex + 1:])
        
        return root
        
        
        
        
        