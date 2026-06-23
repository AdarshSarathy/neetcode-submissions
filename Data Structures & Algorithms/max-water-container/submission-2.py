class Solution:
    def maxArea(self, heights: List[int]) -> int:
        y = len(heights) - 1
        cap = 0
        l, r = 0, y

        while l < r:
            w = r - l
            x = w * min(heights[r], heights[l])

            if x > cap:
                cap = x
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return cap