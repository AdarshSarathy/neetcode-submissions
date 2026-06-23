class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s)-1
        while i-j <= 1:
            print(i, s[i], j, s[j])
            if s[i] != s[j]:
                if s[i].isalnum() and s[j].isalnum():
                    return False
                elif s[i].isalnum():
                    j-=1
                    continue
                else:
                    i+=1
                    continue
            i+=1
            j-=1
        return True