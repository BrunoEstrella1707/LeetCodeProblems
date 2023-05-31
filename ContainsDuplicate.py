class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort() # ordena os números
        for i in range(0, len(nums)-1): # percorre a lista até o penúltimo número
            if nums[i] == nums[i+1]: # verifica se o número atual é igual ao seguinte
                return True
        return False
# Com os números ordenados basta apenas verificar o número seguinte ao iterado