class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = []
        d = dict()
        for i in nums:
            if (i in d):
                d[i] += 1
            else:
                d[i] = 1
        c = sorted(d.values(), reverse = True)
        for i in c[:k]:
            for j in d:
                if d[j] == i and j not in ret:
                    ret.append(j)
        
        return ret
            