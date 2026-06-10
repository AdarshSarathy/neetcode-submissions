class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x, y = set(s), set(t)
        result = []
        if x == y:
            for i in x:
                if s.count(i) == t.count(i):
                    result.append(True)
                else:
                    return False
            if len(result) == len(x):
                return True
        else:
            return False