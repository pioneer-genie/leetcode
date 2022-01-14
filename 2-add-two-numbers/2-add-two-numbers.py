# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = node = ListNode()
        up = 0
        while(l1 or l2):
            node.next = ListNode()
            node = node.next
            node.val += up
            if (l1):
                node.val += l1.val
                l1 = l1.next
            if (l2):
                node.val += l2.val
                l2 = l2.next
            
            up = node.val // 10
            node.val = node.val % 10
        
        if (up):
            node.next = ListNode()
            node.next.val = up
        
        return root.next