class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        res = 0
        count = 1
        nums = sorted(nums)
        if len(nums) == 0: # Se a lista for vazia retorna o resultado
            return res
        for i in range(0, len(nums)-1):
            print(nums[i])
            if nums[i] == nums[i+1]: # Verifica se o número é igual ao seguinte, caso for a sequência se mantém
                continue
            elif nums[i+1] - nums[i] == 1: # Se a diferença entre o seguinte e o atual for 1 eles estão em sequência
                count += 1 # Aumenta o contador
            else: # Nesse caso a sequência é quebrada
                if count > res: # Se a atual contagem for maior que o resultado atual eles são atualizados
                    res = count
                count = 1 
        res = max(res, count)
        return res
                
            