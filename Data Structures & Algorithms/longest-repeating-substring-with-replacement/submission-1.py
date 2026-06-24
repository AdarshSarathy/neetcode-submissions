class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        characterMap = defaultdict(int)
        len_sub = 0
        left = 0

        for right in range(len(s)):
            characterMap[s[right]] += 1
            window_length = right - left + 1
            if window_length - max(characterMap.values()) > k:
                characterMap[s[left]] -= 1
                left += 1
            len_sub = max(len_sub, right - left + 1)
        return len_sub