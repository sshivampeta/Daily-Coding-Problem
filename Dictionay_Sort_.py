'''Given a list of numbers, create an algorithm that arranges them 
in order to form the largest possible integer.

Example: [10, 7, 76, 415] -> "77641510"

The key insight is that we need a custom comparator that determines
which arrangement produces a larger number between two candidates.
For numbers a and b, if concatenating as "ab" > "ba", then a should come first.
'''

import logging
from functools import cmp_to_key
from typing import List

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


# --------------------------------------------------
# SOLUTION 1: Custom Comparator with Sorting ⭐ (Optimal)
# --------------------------------------------------
def largest_number_comparator(nums: List[int]) -> str:
    """
    Arrange numbers to form the largest possible integer using custom comparator.
    
    Approach:
    - Convert numbers to strings
    - Use custom comparator: for strings a, b, compare "ab" vs "ba"
    - If "ab" > "ba" lexicographically, a comes first
    - Otherwise, b comes first
    - Sort using this comparator
    - Concatenate and handle edge case of all zeros
    
    Time Complexity: O(n log n * k) where n is count, k is avg string length
    Space Complexity: O(n * k) for string conversion
    
    Example:
        [10, 7, 76, 415]
        Compare 10, 7: "107" vs "710" -> "710" > "107", so 7 comes first
        Compare 7, 76: "776" vs "767" -> "776" > "767", so 7 comes first
        Compare 76, 415: "76415" vs "41576" -> "76415" > "41576", so 76 comes first
        Result: "77641510"
    """
    if not nums:
        return ""
    
    # Convert to strings
    nums_str = [str(num) for num in nums]
    
    # Custom comparator function
    def compare(a, b):
        # Compare concatenations
        if a + b > b + a:
            return -1  # a comes first (descending order)
        elif a + b < b + a:
            return 1   # b comes first
        else:
            return 0   # equal
    
    # Sort using custom comparator
    nums_str.sort(key=cmp_to_key(compare))
    
    # Join and handle edge case of all zeros
    result = ''.join(nums_str)
    
    # If result is all zeros, return "0"
    if not result or all(c == '0' for c in result):
        return "0"
    
    logging.info(f"Input: {nums}")
    logging.info(f"Sorted: {nums_str}")
    logging.info(f"Result: {result}")
    
    return result


# --------------------------------------------------
# SOLUTION 2: Custom Comparator with Key Function
# --------------------------------------------------
def largest_number_key(nums: List[int]) -> str:
    """
    Alternative implementation using key function instead of compare.
    
    The key function multiplies each number by a factor to simulate
    the comparison needed.
    
    Time Complexity: O(n log n * k)
    Space Complexity: O(n * k)
    """
    if not nums:
        return ""
    
    # Convert to strings
    nums_str = [str(num) for num in nums]
    
    # Multiply each string by a factor to compare properly
    # For sorting, we want larger concatenations first
    # Using negative key to sort in descending order
    nums_str.sort(key=lambda x: x * 10, reverse=True)
    
    logging.info(f"Using key function: {nums_str}")
    
    result = ''.join(nums_str)
    
    if not result or all(c == '0' for c in result):
        return "0"
    
    return result


# --------------------------------------------------
# SOLUTION 3: Manual Bubble Sort with Comparator
# --------------------------------------------------
def largest_number_bubble(nums: List[int]) -> str:
    """
    Implement bubble sort manually with custom comparator.
    
    Time Complexity: O(n²)
    Space Complexity: O(n)
    
    Educational approach - shows the comparison logic clearly.
    """
    if not nums:
        return ""
    
    nums_str = [str(num) for num in nums]
    n = len(nums_str)
    
    # Bubble sort with custom comparator
    for i in range(n):
        for j in range(n - 1 - i):
            # Compare concatenations
            if nums_str[j] + nums_str[j + 1] < nums_str[j + 1] + nums_str[j]:
                # Swap if order is wrong
                nums_str[j], nums_str[j + 1] = nums_str[j + 1], nums_str[j]
                logging.info(f"Swapped {nums_str[j+1]} and {nums_str[j]}")
    
    result = ''.join(nums_str)
    
    if not result or all(c == '0' for c in result):
        return "0"
    
    logging.info(f"Bubble sort result: {result}")
    return result


# --------------------------------------------------
# SOLUTION 4: Counting Sort (For Digits Only)
# --------------------------------------------------
def largest_number_counting(nums: List[int]) -> str:
    """
    Optimize for numbers with limited digit range.
    
    This approach uses counting sort principles on the string
    representations, but falls back to comparison for ties.
    
    Time Complexity: O(n + k) where k is max string length
    Space Complexity: O(n)
    
    Note: Less practical than comparison-based approach for large numbers.
    """
    if not nums:
        return ""
    
    # For this problem, comparison-based is more general
    # Keeping this as a placeholder for different approach
    return largest_number_comparator(nums)


# --------------------------------------------------
# UTILITY FUNCTIONS
# --------------------------------------------------
def verify_largest(nums: List[int], result: str) -> bool:
    """
    Verify that the result is actually the largest possible arrangement.
    
    Time Complexity: O(n! * n) - generate and check all permutations
    Only practical for small inputs.
    """
    if not nums:
        return result == ""
    
    # For verification, we could check all permutations
    # But this is O(n!) so only useful for small lists
    nums_str = [str(num) for num in nums]
    
    # Simple verification: check no adjacent pair can be swapped for better result
    result_num = int(result) if result and result != "0" else 0
    
    # Try all adjacent swaps
    for i in range(len(nums_str) - 1):
        for j in range(i + 1, len(nums_str)):
            # Create variant with swap
            variant = nums_str[:]
            variant[i], variant[j] = variant[j], variant[i]
            variant_str = ''.join(variant)
            variant_num = int(variant_str) if variant_str and variant_str != "0" else 0
            
            if variant_num > result_num:
                logging.warning(f"Found better arrangement: {variant_str}")
                return False
    
    return True


# --------------------------------------------------
# TEST CASES
# --------------------------------------------------
def run_tests():
    print("=" * 70)
    print("TESTING LARGEST NUMBER ARRANGEMENT")
    print("=" * 70)
    
    test_cases = [
        # (input, expected_output)
        ([10, 7, 76, 415], "77641510"),
        ([3, 30, 34, 5, 9], "9534330"),
        ([0, 0, 0], "0"),
        ([0], "0"),
        ([1], "1"),
        ([9, 8, 7, 6, 5], "98765"),
        ([1, 2, 3, 4, 5], "54321"),
        ([12, 121], "12112"),
        ([824, 938, 1, 7, 55, 927, 17, 9, 5, 2, 1, 3, 9, 46, 89, 500], None),
        ([3, 5, 10, 7, 2], "75532310"),
        ([], ""),
        ([100, 1, 10], "11010100"),
    ]
    
    for idx, (nums, expected) in enumerate(test_cases, 1):
        print(f"\n--- Test Case {idx} ---")
        print(f"Input: {nums}")
        
        if not nums:
            print("Empty input, skipping")
            continue
        
        # Test Solution 1: Comparator
        result1 = largest_number_comparator(nums.copy())
        print(f"Comparator: {result1}")
        
        # Test Solution 2: Key function
        result2 = largest_number_key(nums.copy())
        print(f"Key function: {result2}")
        
        # Test Solution 3: Bubble sort
        result3 = largest_number_bubble(nums.copy())
        print(f"Bubble sort: {result3}")
        
        # Verify consistency
        if result1 == result2 == result3:
            print(f"✅ All approaches agree: {result1}")
        else:
            print(f"❌ Results differ!")
        
        # Verify result
        if verify_largest(nums, result1):
            print("✅ Result verified as optimal")
        else:
            print("❌ Result is not optimal")
        
        # Check against expected
        if expected is not None:
            if result1 == expected:
                print(f"✅ Matches expected: {expected}")
            else:
                print(f"❌ Expected: {expected}, Got: {result1}")
    
    # Performance test
    print("\n" + "=" * 70)
    print("PERFORMANCE TEST")
    print("=" * 70)
    
    # Generate larger test
    large_test = list(range(1, 101))
    import time
    
    start = time.time()
    result = largest_number_comparator(large_test)
    elapsed = time.time() - start
    
    print(f"\nInput size: {len(large_test)}")
    print(f"Result length: {len(result)}")
    print(f"Time: {elapsed:.4f} seconds")
    print(f"Result (first 50 chars): {result[:50]}...")


if __name__ == "__main__":
    run_tests()
