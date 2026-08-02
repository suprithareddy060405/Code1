def productExceptSelf(nums: list[int]) -> list[int]:
    """
    Given an integer array nums, returns an array answer such that
    answer[i] is equal to the product of all the elements of nums except nums[i].
    
    Time Complexity: O(n)
    Space Complexity: O(1) auxiliary space (excluding the output array)
    """
    n = len(nums)
    answer = [1] * n
    
    # Step 1: Calculate prefix products.
    # answer[i] will contain the product of all elements to the left of i.
    for i in range(1, n):
        answer[i] = answer[i - 1] * nums[i - 1]
        
    # Step 2: Calculate suffix products and combine them.
    # We use a running suffix product variable to maintain O(1) auxiliary space.
    suffix_prod = 1
    for i in range(n - 1, -1, -1):
        # Multiply prefix product (already in answer[i]) with suffix product
        answer[i] *= suffix_prod
        # Update running suffix product for the next iteration (index i-1)
        suffix_prod *= nums[i]
        
    return answer

# Sample Input & Output:
# Example 1:
#   Input:  nums = [1, 2, 3, 4]
#   Output: [24, 12, 8, 6]
#
# Example 2:
#   Input:  nums = [-1, 1, 0, -3, 3]
#   Output: [0, 0, 9, 0, 0]

if __name__ == '__main__':
    # Test case 1
    nums1 = [1, 2, 3, 4]
    result1 = productExceptSelf(nums1)
    print(f"Input: {nums1} -> Output: {result1}")
    assert result1 == [24, 12, 8, 6], f"Test case 1 failed: expected [24, 12, 8, 6], got {result1}"
    
    # Test case 2
    nums2 = [-1, 1, 0, -3, 3]
    result2 = productExceptSelf(nums2)
    print(f"Input: {nums2} -> Output: {result2}")
    assert result2 == [0, 0, 9, 0, 0], f"Test case 2 failed: expected [0, 0, 9, 0, 0], got {result2}"
    
    print("All test cases passed successfully!")
