class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = 0
        while left <= right:
            mid = (right + left) // 2

            if nums[mid-1] > nums[mid]:
                return nums[mid]
            else:
                if nums[right] > nums[left]:
                    
                    right = mid - 1
                else:
                    while left < mid + 1:
                        if nums[left-1] < nums[left]:
                            left += 1
                        else:
                            return nums[left]
                    # left = mid + 1
            
            print(left, mid, right)
        
        # return nums[mid]