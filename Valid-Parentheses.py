class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}  # Mapping pasangan tanda kurung

        for char in s:
            if char in "({[":  # Jika karakter adalah tanda buka, push ke stack
                stack.append(char)
            else:  # Jika karakter adalah tanda tutup
                if not stack or stack[-1] != pairs[char]:  # Periksa pasangan terakhir di stack
                    return False
                stack.pop()  # Pop elemen terakhir jika pasangan cocok

        return len(stack) == 0  
            
        


            

        