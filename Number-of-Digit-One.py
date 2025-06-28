class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        factor = 1  # Faktor untuk menentukan posisi digit (1, 10, 100, ...)
        
        while factor <= n:
            left_part = n // (factor * 10)  # Bagian kiri dari angka
            current_digit = (n // factor) % 10  # Digit yang sedang dihitung
            right_part = n % factor  # Bagian kanan dari angka

            if current_digit == 0:
                count += left_part * factor
            elif current_digit == 1:
                count += left_part * factor + right_part + 1
            else:
                count += (left_part + 1) * factor

            factor *= 10  # Pindah ke digit berikutnya
        
        return count
        # if n == 0:
        #     return 0
        # if n < 10:
        #     return 1
        # count = 1
        # for i in range(10, n+1):
        #     i = str(i)
        #     for s in i:
        #         if s == '1':
        #             count += 1
        
        return count



