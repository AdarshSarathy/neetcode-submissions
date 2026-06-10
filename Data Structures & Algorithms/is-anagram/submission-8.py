class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x, y = set(s), set(t)
        if x == y:
            for i in x:
                if s.count(i) != t.count(i):
                    return False
            return True
        else:
            return False