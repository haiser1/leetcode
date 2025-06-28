class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        angka = 0
        i = 0
        while i < len(s):
            # Cek apakah ada simbol dua karakter seperti IV, IX, dll.
            if i + 1 < len(s) and s[i:i+2] in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                if s[i] == 'I' and s[i+1] == 'V':
                    angka += 4
                elif s[i] == 'I' and s[i+1] == 'X':
                    angka += 9
                elif s[i] == 'X' and s[i+1] == 'L':
                    angka += 40
                elif s[i] == 'X' and s[i+1] == 'C':
                    angka += 90
                elif s[i] == 'C' and s[i+1] == 'D':
                    angka += 400
                elif s[i] == 'C' and s[i+1] == 'M':
                    angka += 900
                i += 2  # Lewati dua karakter
            else:
                angka += roman_to_int[s[i]]
                i += 1  # Lewati satu karakter
        return angka