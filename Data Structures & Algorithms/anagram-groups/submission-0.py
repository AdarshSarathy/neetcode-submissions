class Solution:
    def groupAnagrams(self, strs: List[str]):# -> List[List[str]]:
        dic = {}
        for i in strs:
            x = list(i)
            x.sort()
            x = tuple(x)
            if x not in dic:
                dic[x] = [i]
            else:
                dic[x] += [i]
        
        return list(dic.values())
