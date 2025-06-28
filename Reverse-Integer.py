class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1 # cek jika nilai negatif atau positif, jika postif nilainya 1 jika negatif nilainya -1

        reverse_num = int(str(abs(x))[::-1]) # uabh nilai ke string lalu di reverse lalu di ubah lagi ke int dan di jadikan nilai absolute

        result = reverse_num * sign # hasil dari reverse di kalikan sign

        # untuk mengecek jika nilai nya melebihi dari range int
        if result < -2**31 or result > 2**31 - 1: 
            return 0 
        
        return result

            
