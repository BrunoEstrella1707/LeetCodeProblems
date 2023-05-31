class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums)) # Resposta
        prefix = 1 # Inicializa a variável que guardará as multiplicações anteriores
        for i in range(0, len(nums)):
            res[i] = prefix # Adiciona a multiplicação à posição atual
            prefix *= nums[i] # Multiplica o número atual pelos seus antecessores
        postfix = 1 # Inicializa a variável que guardará as multiplicações posteriores
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix # Multiplica o resultado da multiplicação dos posteriores pelos anteriores
            postfix *= nums[i] # Multiplica o número atual pelos seus sucessores
        return res
# Percorre a lista nos dois sentidos, de forma que quando percorrida do início ao fim, guardará a multiplicação dos números anteriores ao atual.
# Quando percorrida do final ao início, guarda as multiplicações dos números posteriores ao atual
