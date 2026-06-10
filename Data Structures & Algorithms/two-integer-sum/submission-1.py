class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_map = {}
        for i,j in enumerate(nums):
            if j not in difference_map:
                difference_map[target-j] = i
            else:
                return [difference_map[j],i]