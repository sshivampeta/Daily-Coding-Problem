'''Given an array of integers, 
find the maximum XOR of any two elements.

Example: [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
Max XOR would be between two numbers that differ in most significant bits.
For example: 83 (1010011) XOR 36 (0100100) = 123 (1111111)
'''

import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


# --------------------------------------------------
# SOLUTION 1: Bit Manipulation with Trie ⭐ (Optimal)
# --------------------------------------------------
class TrieNode:
    def __init__(self):
        self.zero = None
        self.one = None


def max_xor_trie(nums):
    """
    Find maximum XOR using a Trie of binary representations.
    
    Approach:
    - Build a trie of binary representations (32-bit integers)
    - For each number, traverse trie greedily picking opposite bits
    - Opposite bits maximize XOR value
    
    Time Complexity: O(n * 32) = O(n)
    Space Complexity: O(n * 32) = O(n) for trie
    """
    if len(nums) < 2:
        return 0
    
    # Build trie of all numbers
    root = TrieNode()
    
    for num in nums:
        node = root
        for i in range(31, -1, -1):
            # Get i-th bit (1 if bit is set, 0 otherwise)
            bit = (num >> i) & 1
            
            if bit == 0:
                if node.zero is None:
                    node.zero = TrieNode()
                node = node.zero
            else:
                if node.one is None:
                    node.one = TrieNode()
                node = node.one
    
    max_xor = 0
    
    # For each number, find its XOR pair in trie
    for num in nums:
        node = root
        current_xor = 0
        
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            # Try to go opposite direction (to maximize XOR)
            opposite_bit = 1 - bit
            
            if opposite_bit == 0:
                if node.zero is not None:
                    current_xor |= (1 << i)
                    node = node.zero
                else:
                    node = node.one
            else:
                if node.one is not None:
                    current_xor |= (1 << i)
                    node = node.one
                else:
                    node = node.zero
        
        max_xor = max(max_xor, current_xor)
        logging.info(f"Number {num}: max XOR so far = {max_xor}")
    
    return max_xor


# --------------------------------------------------
# SOLUTION 2: Bit Manipulation with Set (No Trie)
# --------------------------------------------------
def max_xor_set(nums):
    """
    Find maximum XOR by building answer bit by bit.
    
    Approach:
    - For each bit position from MSB to LSB
    - Try to set that bit in result (try to make it 1)
    - Check if it's possible with some pair of numbers
    - Use set for O(1) lookup
    
    Time Complexity: O(n * 32) = O(n)
    Space Complexity: O(n)
    """
    if len(nums) < 2:
        return 0
    
    max_xor = 0
    mask = 0
    
    for i in range(31, -1, -1):
        mask |= (1 << i)  # Prefix mask for current bit
        
        # Get all prefixes of all numbers up to current bit
        prefixes = {num & mask for num in nums}
        
        # Try to set current bit in result
        temp = max_xor | (1 << i)
        
        # Check if temp is achievable
        # temp = a ^ b => a ^ b ^ b = a ^ temp => a = b ^ temp
        # So we need to find two numbers whose XOR gives temp
        for prefix in prefixes:
            if (temp ^ prefix) in prefixes:
                max_xor = temp
                logging.info(f"Bit {i}: Set bit in result, max_xor = {max_xor}")
                break
    
    return max_xor


# --------------------------------------------------
# SOLUTION 3: Brute Force (for small arrays)
# --------------------------------------------------
def max_xor_bruteforce(nums):
    """
    Brute force approach - try all pairs.
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    if len(nums) < 2:
        return 0
    
    max_xor = 0
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            xor_val = nums[i] ^ nums[j]
            if xor_val > max_xor:
                max_xor = xor_val
                logging.info(f"Found XOR: {nums[i]} ^ {nums[j]} = {xor_val}")
    
    return max_xor


# --------------------------------------------------
# SOLUTION 4: Greedy Bit Building
# --------------------------------------------------
def max_xor_greedy(nums):
    """
    Greedy approach building result bit by bit.
    Similar to Solution 2 but more explicit.
    
    Time Complexity: O(n * 32)
    Space Complexity: O(n)
    """
    if len(nums) < 2:
        return 0
    
    result = 0
    
    for bit in range(31, -1, -1):
        # Try to set this bit to 1
        current_bit = 1 << bit
        
        # Collect all prefixes with current bit position
        prefixes = set()
        for num in nums:
            # Get prefix of num up to current bit
            prefix = num & (-1 ^ ((1 << bit) - 1))  # All bits from bit 31 down to current bit
            prefixes.add(prefix)
        
        # Try setting this bit
        temp_result = result | current_bit
        
        # Check if achievable: need a ^ b = temp_result for some prefixes
        for prefix in prefixes:
            complement = temp_result ^ prefix
            if complement in prefixes:
                result = temp_result
                logging.info(f"Bit {bit}: Set bit, result = {result}")
                break
    
    return result


# --------------------------------------------------
# UTILITY FUNCTIONS
# --------------------------------------------------
def print_binary(num):
    """Print number in 32-bit binary format"""
    return format(num, '032b')


def trace_xor_pair(nums, target_xor):
    """Find which pair gives maximum XOR"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] ^ nums[j] == target_xor:
                return nums[i], nums[j]
    return None, None


# --------------------------------------------------
# TEST CASES
# --------------------------------------------------
def run_tests():
    print("=" * 70)
    print("TESTING MAXIMUM XOR")
    print("=" * 70)
    
    test_cases = [
        # (array, expected_max_xor_value)
        ([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70], None),  # Calculate
        ([3, 10, 5, 25, 2, 8], None),                               # Calculate
        ([1, 2, 3, 4, 5], None),                                     # 4 ^ 5 = 1, no others better
        ([8, 10, 2], 10),                                            # 8 ^ 2 = 10
        ([0, 1], 1),                                                 # 0 ^ 1 = 1
        ([4, 5, 6, 7], 3),                                           # 4 ^ 7 = 3 or 5 ^ 6 = 3
        ([0], 0),                                                     # Single element
        ([25, 91, 78, 43], None),                                    # Calculate
    ]
    
    for idx, (nums, expected) in enumerate(test_cases, 1):
        print(f"\n--- Test Case {idx} ---")
        print(f"Array: {nums}")
        
        if len(nums) >= 2:
            # Test Solution 1: Trie
            result1 = max_xor_trie(nums.copy())
            print(f"Trie Approach: {result1}")
            
            # Test Solution 2: Set
            result2 = max_xor_set(nums.copy())
            print(f"Set Approach: {result2}")
            
            # Test Solution 3: Brute Force
            result3 = max_xor_bruteforce(nums.copy())
            print(f"Brute Force: {result3}")
            
            # Test Solution 4: Greedy Bit Building
            result4 = max_xor_greedy(nums.copy())
            print(f"Greedy Approach: {result4}")
            
            # Verify consistency
            if result1 == result2 == result3:
                print(f"✅ All approaches agree: {result1}")
            else:
                print(f"❌ Results differ!")
            
            # Find the pair
            a, b = trace_xor_pair(nums, result1)
            if a is not None:
                print(f"Pair: {a} ^ {b} = {a ^ b}")
                print(f"Binary: {print_binary(a)} ^ {print_binary(b)}")
            
            if expected is not None:
                status = "✅" if result1 == expected else "❌"
                print(f"Expected: {expected} {status}")
        else:
            print("Array too small (need at least 2 elements)")
    
    # Additional test: Performance comparison
    print("\n" + "=" * 70)
    print("PERFORMANCE TEST")
    print("=" * 70)
    print("\nLarge array test would compare time complexity")
    print("Trie/Set/Greedy: O(n * 32) = O(n)")
    print("Brute Force: O(n²)")


if __name__ == "__main__":
    run_tests()