# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        
        result = []

        for lst in lists:
            curr = lst

            while curr:
                result.append(curr.val)
                curr = curr.next


        dummy = ListNode()
        tail = dummy

        result.sort()

        for val in result:
            tail.next = ListNode(val)
            tail = tail.next        


        return dummy.next     

            