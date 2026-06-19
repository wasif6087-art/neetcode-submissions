# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        from collections import deque

        q = deque()
        q.append(root)

        sorted_vals = []

        while q:
            node = q.popleft()

            # insert node.val into sorted_vals in correct position
            inserted = False
            for i in range(len(sorted_vals)):
                if node.val < sorted_vals[i]:
                    sorted_vals.insert(i, node.val)
                    inserted = True
                    break

            if not inserted:
                sorted_vals.append(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return sorted_vals[k - 1]


