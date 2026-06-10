class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_map = {}
        j=0
        for i in nums:
            x = target-i
            if i not in difference_map:
                difference_map[x] = j
            else:
                return [difference_map[i],j]
            j+=1