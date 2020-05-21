"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
        def kthSmallest(self, root: TreeNode, k: int) -> int:
                l = []
                def inOrder(node):
                        if not node:
                                return 
                        inOrder(node.left)
                        l.append(node.val)
                        inOrder(node.right)
                inOrder(root)
                print(l)
                return l[k - 1]