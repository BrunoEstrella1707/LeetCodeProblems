class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = dict()
        for i in strs:
            res[tuple(sorted(i))] = [] # Cria um dicionário onde os valores são listas e as chaves são as palavras ordenadas
        for i in strs:
            res[tuple(sorted(i))].append(i) # Insere a palavra na posição de acordo com sua ordenação, logo anagramas estarão na mesma posição
        return res.values()
    





