def productExceptSelf(nums: List[int]) -> List[int]:
    left_product, right_product = [1] * len(nums), [1] * len(nums)
    for i in range(1, len(nums)):
        left_product[i] = nums[i - 1] * left_product[i - 1]
    for i in range(len(nums) - 2, -1, -1):
        right_product[i] = nums[i + 1] * right_product[i + 1]

    return [left_product[i] * right_product[i] for i in range(len(nums))]