class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if len(s) != len(t):
            return False
        else:
            for i in range(0, len(s)):
                if s[i] != t[i]:
                    return False
            return True
# Ordena ambas palavras e as percorre verificando cada letra