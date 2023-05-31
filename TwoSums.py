class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pmap = {}
        for i, n in enumerate(nums):
            diff = target - n # Verifica a diferença entre o número atual e o alvo
            if diff in pmap: # Caso a diferença esteja no mapa, significa que existe um número na lista que ao somar chegará ao alvo
                return [pmap[diff], i]
            pmap[n] = i # Adiciona o índice como valor na posição onde seu valor da lista é chave

            