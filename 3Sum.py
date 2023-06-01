class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums = sorted(nums) # Para a solução funcionar a lista precisa estar ordenada

        for i, n in enumerate(nums): # Itera sobre cada número na lista
            if i > 0 and n == nums[i-1]: # verifica se o número é repetido
               continue
            l, r = i+1, len(nums)-1 # inicializa dois ponteiros, direito e esquerdo
            while l < r: # Enquanto os ponteiros forem diferente ele continua o loop
                sum_3 = n + nums[l] + nums[r] # Verifica a soma dos 3 números
                if sum_3 > 0: # Caso a soma seja positiva é necessário um número menor, mudando o ponteiro da direita
                    r  -= 1
                elif sum_3 < 0:  # Caso a soma seja negativa é necessário um número maior, mudando o ponteiro da esquerda
                    l += 1
                elif sum_3 == 0: # Soma dos 3 números igual a 0, monta a lista e a adiciona a resposta
                    res.append([n, nums[l], nums[r]])
                    l += 1 # Muda o ponteiro da esquerda
                    while nums[l] == nums[l-1] and l < r: # Caso o número seguinte seja igual ao atual atualiza o ponteiro da esquerda
                        l += 1
        return res