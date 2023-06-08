class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tam = len(s2) - len(s1) + 1
        for r in range(0, tam):
            fim = r + (len(s1)) 
            if sorted(s1) == sorted(s2[r:fim]):
                return True
        return False
            



