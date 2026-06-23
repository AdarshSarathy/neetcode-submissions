class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            num_sum = numbers[l] + numbers[r]
            diff = target - num_sum
            if diff > 0:
                l+=1
            elif diff < 0:
                r-=1
            else:
                l+=1
                r+=1
                break

        return [l, r]