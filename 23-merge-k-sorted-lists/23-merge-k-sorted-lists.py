# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = []
        for lst in lists:
            while(lst):
                heapq.heappush(hq, lst.val)
                lst = lst.next
                
        root = ListNode()
        ret = root
        
        while(hq):
            ret.next = ListNode(heapq.heappop(hq))
            ret = ret.next
        
        return root.next