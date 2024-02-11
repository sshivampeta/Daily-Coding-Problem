'''
Given an array of numbers N and an integer k, 
your task is to split N into k partitions such that the 

maximum sum of any partition is minimized. Return this sum.

For example, given N = [5, 1, 2, 7, 3, 4] and k = 3,
 you should return 8, since the optimal partition is [5, 1, 2], 
 [7], [3, 4] 
'''

import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


# --------------------------------------------------
# SOLUTION 1: Binary Search + Greedy ⭐ (Optimal)
# --------------------------------------------------
def partition_array_binary_search(N, k):
    """
    Minimize the maximum sum of any partition using binary search.
    
    Approach:
    - Answer is in range [max(N), sum(N)]
    - Binary search on this range
    - For each candidate max_sum, check if valid partition exists using greedy
    
    Time Complexity: O(n * log(sum(N)))
    Space Complexity: O(1)
    """
    if k == 1:
        return sum(N)
    if k >= len(N):
        return max(N)
    
    def can_partition(max_sum):
        """Check if we can partition array into k parts with each sum <= max_sum"""
        partitions = 1
        current_sum = 0
        
        for num in N:
            if current_sum + num <= max_sum:
                current_sum += num
            else:
                # Start a new partition
                partitions += 1
                current_sum = num
                
                if partitions > k:
                    return False
        
        return partitions <= k
    
    # Binary search bounds
    left = max(N)  # Minimum possible maximum sum
    right = sum(N)  # Maximum possible maximum sum
    
    logging.info(f"Binary search range: [{left}, {right}]")
    
    while left < right:
        mid = (left + right) // 2
        logging.info(f"Testing mid={mid}")
        
        if can_partition(mid):
            # If possible, try to reduce further
            right = mid
        else:
            # If not possible, need larger max_sum
            left = mid + 1
    
    logging.info(f"Answer found: {left}")
    return left


# --------------------------------------------------
# SOLUTION 2: Dynamic Programming
# --------------------------------------------------
def partition_array_dp(N, k):
    """
    Dynamic programming approach.
    
    dp[i][j] = minimum maximum partition sum for first i elements in j partitions
    
    Time Complexity: O(n² * k)
    Space Complexity: O(n * k)
    """
    n = len(N)
    
    if k == 1:
        return sum(N)
    if k >= n:
        return max(N)
    
    # Prefix sum for quick range sum calculation
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + N[i]
    
    def range_sum(i, j):
        """Sum of elements from index i to j (inclusive)"""
        return prefix[j + 1] - prefix[i]
    
    # dp[i][j] = min max sum to partition N[0:i] into j partitions
    # Initialize with infinity
    INF = float('inf')
    dp = [[INF] * (k + 1) for _ in range(n + 1)]
    
    # Base case: 0 elements in j partitions
    dp[0][0] = 0
    
    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            # Try all possible positions for the last partition
            for p in range(j - 1, i):
                # Last partition is from p to i-1
                last_partition_sum = range_sum(p, i - 1)
                current_max = max(dp[p][j - 1], last_partition_sum)
                dp[i][j] = min(dp[i][j], current_max)
    
    logging.info(f"DP solution: {dp[n][k]}")
    return dp[n][k]


# --------------------------------------------------
# SOLUTION 3: Greedy with Backtracking
# --------------------------------------------------
def partition_array_greedy(N, k):
    """
    Greedy approach: fill partitions one by one.
    Uses binary search to find the minimum possible maximum sum.
    Similar to Solution 1 but with more detailed logging.
    
    Time Complexity: O(n * log(sum(N)))
    Space Complexity: O(k)
    """
    if k == 1:
        return sum(N)
    if k >= len(N):
        return max(N)
    
    def partition_with_limit(max_sum):
        """Returns number of partitions needed if each partition <= max_sum"""
        partitions = 1
        current_sum = 0
        partition_list = []
        current_partition = []
        
        for num in N:
            if current_sum + num <= max_sum:
                current_sum += num
                current_partition.append(num)
            else:
                partition_list.append((current_partition, current_sum))
                current_partition = [num]
                current_sum = num
                partitions += 1
        
        partition_list.append((current_partition, current_sum))
        
        return partitions, partition_list
    
    left = max(N)
    right = sum(N)
    
    while left < right:
        mid = (left + right) // 2
        num_partitions, partitions = partition_with_limit(mid)
        
        logging.info(f"Testing max_sum={mid}: needs {num_partitions} partitions")
        
        if num_partitions <= k:
            logging.info(f"  Partitions: {partitions}")
            right = mid
        else:
            left = mid + 1
    
    _, final_partitions = partition_with_limit(left)
    logging.info(f"Final partitions: {final_partitions}")
    
    return left


# --------------------------------------------------
# TEST CASES
# --------------------------------------------------
def run_tests():
    test_cases = [
        # (N, k, expected)
        ([5, 1, 2, 7, 3, 4], 3, 8),
        ([1, 2, 3, 4, 5], 2, 7),  # [1,2,4] [5] or [1,2,3] [4,5]
        ([1], 1, 1),
        ([1, 2, 3], 1, 6),
        ([1, 2, 3], 3, 3),
        ([10], 1, 10),
        ([4, 3, 2, 6, 5, 1], 3, 8),
        ([1, 1, 1, 1, 1, 1], 2, 3),
    ]
    
    print("\n" + "=" * 70)
    print("TESTING PARTITION ARRAY SOLUTIONS")
    print("=" * 70)
    
    for idx, (N, k, expected) in enumerate(test_cases, 1):
        print(f"\n--- Test Case {idx} ---")
        print(f"N = {N}, k = {k}")
        print(f"Expected: {expected}")
        
        # Test Solution 1: Binary Search
        result1 = partition_array_binary_search(N.copy(), k)
        print(f"Binary Search: {result1} {'✅' if result1 == expected else '❌'}")
        
        # Test Solution 2: DP
        result2 = partition_array_dp(N.copy(), k)
        print(f"Dynamic Programming: {result2} {'✅' if result2 == expected else '❌'}")
        
        # Test Solution 3: Greedy
        result3 = partition_array_greedy(N.copy(), k)
        print(f"Greedy with Backtracking: {result3} {'✅' if result3 == expected else '❌'}")


if __name__ == "__main__":
    run_tests()