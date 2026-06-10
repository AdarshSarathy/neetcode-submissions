class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for i in strs:
            list_0 = [0] * 26
            for j in i:
                list_0[ord(j)-ord('a')] += 1
            list_0 = tuple(list_0)
            if list_0 in dic:
                dic[list_0] += [i]
            else:
                dic[list_0] = [i]
        
        return list(dic.values())