class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        def visit_room(i):
            if (i in visit):
                return
            visit.add(i)
            for j in rooms[i]:
                visit_room(j)
        
        visit_room(0)
        
        return len(visit) == len(rooms)
        