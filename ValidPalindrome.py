class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = ''
        r = ''

        for i in s: # Perocorre os carácteres de s
            if i.isalnum(): # Verifica se o caracter é alfanumérico
                n += i.lower() # Adiciona à string o caracter minúsculo
        return n == n[::-1] # Verifica se a string é igual a ela invertida