class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (right + left)//2

        result = -1

        while left <= right:
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid+1
                mid = (right + left)//2
            else:
                right = mid-1
                mid = (right + left)//2
            result = -1 if target != nums[mid] else mid

        return result