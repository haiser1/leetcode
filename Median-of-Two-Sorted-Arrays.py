class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_nums = nums1 + nums2
        merge_nums.sort()
        mid = len(merge_nums) // 2
        if len(merge_nums) % 2 != 0:
            return float(f'{merge_nums[mid]:.5f}')
        result = (merge_nums[mid] + merge_nums[mid-1]) / 2 
        return float(f'{result:.5f}')