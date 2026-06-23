class Solution:
    def maxArea(self, heights: List[int]) -> int:
        y = len(heights) - 1
        cap = 0
        l, r = 0, y
        # print(heights)
        while l < r:
            w = r - l
            # print(w,l,r)
            x = w * min(heights[r], heights[l])
            # print(x)
            
            if x > cap:
                cap = x
            else:
                if r - l == 1:
                    l = 0
                    r -= 1
            
            l += 1
        
        return cap