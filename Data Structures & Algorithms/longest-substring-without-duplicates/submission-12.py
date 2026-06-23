class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        n = len(s)
        if n == 0 or n == 1:
            return n

        substring = set()
        len_sub = 0

        while right < n:
            print(s[left], s[right])
            if s[right] not in substring:
                substring.add(s[right])
            else:
                print(substring)
                len_sub = max(len_sub, right - left)
                while s[right] in substring:
                    substring.remove(s[left])
                    left += 1
                substring.add(s[right])
            right += 1
            print(substring)

        len_sub = max(len_sub, right - left)
        return len_sub
