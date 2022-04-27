class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        str_dict = dict()
        for s in strs:
            sorted_s = "".join(sorted(s))
            if (sorted_s in str_dict):
                str_dict[sorted_s].append(s)
            else:
                str_dict[sorted_s] = [s]
        return [str_dict[i] for i in str_dict]
                    