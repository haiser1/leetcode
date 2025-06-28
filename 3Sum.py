class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()  # Sorting agar mudah menggunakan two-pointer
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip angka yang sama
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip angka yang sama agar hasil unik
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
        
        # result = set()

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if (nums[i]) + (nums[j]) + (nums[k]) == 0:
        #                 triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
        #                 result.add(triplet)

        # return list(map(list, result))
        