class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        boxs = sorted(capacity, reverse=True)
        total_apple = sum(apple)
        result = 0
        
        for box in boxs:
            if total_apple > box:
                total_apple -= box
                result += 1

            elif total_apple > 0:
                total_apple -= box
                result += 1
        return result
