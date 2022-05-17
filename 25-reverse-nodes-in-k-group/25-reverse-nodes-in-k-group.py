# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        node = head
        retRoot = ListNode()
        ret = retRoot
        while(node):
            stack.append(ListNode(node.val))
            if (len(stack) == k):
                while(stack):
                    ret.next = stack.pop()
                    ret = ret.next
            node = node.next
        
        if (stack):
            for i in stack:
                ret.next = i
                ret = ret.next
        
        return retRoot.next
                
            
                
        