class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        bucket = [[] for i in range(len(nums) + 1)] # cria uma lista referente a cada elemento em nums
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0) # Chave do dicionário será o número e o valor a quantidade de vezes em que aparece
        for c, v in count.items():
            bucket[v].append(c) # Cada lista será preenchida com a quantidade de vezes que o número referente àquela lista aparece

        res = []
        for i in range(len(bucket) -1, 0, -1): # Percorre a lista de forma inversa
            for n in bucket[i]: # Percorre a sublista
                res.append(n) # Adiciona os números na lista de resposta
                if len(res) == k: # Caso o tamanho de res seja igual ao de k, significa que os k números foram retornados
                    return res
