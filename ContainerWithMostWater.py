class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        l, r = 0, len(height)-1 # inicializa os dois ponteiros, esquerdo e direito
        while l < r:
            total = (r-l) * min(height[l], height[r]) # verifica a área atual
            res = max(res, total) # verifica se a área calculada agora é maior que a calculada anteriormente
            if height[l] < height[r]: # caso a altura esquerda seja menor, o ponteiro esquerdo muda para a altura a sua esquerda
                l += 1
            else: # caso a altura esquerda seja maior, o ponteiro direito muda para a altura a sua direita
                r -=  1
        return res