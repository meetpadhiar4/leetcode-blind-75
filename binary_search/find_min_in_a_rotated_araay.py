class Solution:
		def findMin(nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if (mid > 0 and mid < len(nums) - 1) and nums[mid - 1] > nums[mid] and nums[mid] < nums[mid + 1]:
                return nums[mid]
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]     
