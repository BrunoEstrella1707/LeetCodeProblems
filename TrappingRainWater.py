class Solution:
    def trap(self, height: list[int]) -> int:
        max_l = [0]
        max_r = [0]
        res = 0
        n_max = 0
        for i in range(1, len(height)):
            n_max = max(height[i-1], n_max)
            max_l.append(n_max)

        n_max = 0
        for i in range(len(height)-2, -1, -1):
            n_max = max(height[i+1], n_max)
            max_r.append(n_max)

        max_r = max_r[::-1]

        for  i in range(0, len(height)):
            x = min(max_r[i], max_l[i]) - height[i]
            if x >= 0:
                res += x
        
        return res


