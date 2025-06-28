class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1:
            hasil = 0
            for i in digits:
                hasil += i + 1
            hasil = [int(digit) for digit in str(hasil)]
            return hasil
        else:
            result = int(''.join(map(str, digits)))
            result += 1
            hasil = [int(digit) for digit in str(result)]
            return hasil
        