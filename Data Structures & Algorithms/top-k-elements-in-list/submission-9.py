class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        buckets = [[] for _ in range(len(nums)+1)]

        for i,j in dic.items():
            buckets[j].append(i)

        result = []
        n = 0

        for i in buckets[::-1]:
            if len(i) > 0 and n < k:
                for j in i:
                    result.append(j)
                    n+=1

        return result