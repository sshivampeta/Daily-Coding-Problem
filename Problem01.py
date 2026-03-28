'''

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?'''

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


# --------------------------------------------------
# 1. ONE-PASS HASH SET (Optimal)
# --------------------------------------------------
def has_pair_one_pass(nums, k):
    seen = set()
    for num in nums:
        complement = k - num
        logging.info(f"Checking num={num}, complement={complement}, seen={seen}")

        if complement in seen:
            logging.info(f"Pair found: ({num}, {complement})")
            return True

        seen.add(num)

    return False


# --------------------------------------------------
# 2. TWO-PASS HASH MAP (Handles duplicates explicitly)
# --------------------------------------------------
def has_pair_two_pass(nums, k):
    counts = {}

    # First pass: count occurrences
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    logging.info(f"Counts map: {counts}")

    # Second pass: check pairs
    for num in nums:
        complement = k - num

        if complement in counts:
            # Case: same number twice (e.g., 5 + 5 = 10)
            if complement == num:
                if counts[num] > 1:
                    logging.info(f"Pair found (duplicate case): ({num}, {num})")
                    return True
            else:
                logging.info(f"Pair found: ({num}, {complement})")
                return True

    return False


# --------------------------------------------------
# 3. TWO POINTERS (SORTING)
# --------------------------------------------------
def has_pair_two_pointers(nums, k):
    nums = sorted(nums)
    left, right = 0, len(nums) - 1

    logging.info(f"Sorted nums: {nums}")

    while left < right:
        s = nums[left] + nums[right]
        logging.info(f"Checking: {nums[left]} + {nums[right]} = {s}")

        if s == k:
            logging.info(f"Pair found: ({nums[left]}, {nums[right]})")
            return True
        elif s < k:
            left += 1
        else:
            right -= 1

    return False


# --------------------------------------------------
# 4. BRUTE FORCE (All pairs)
# --------------------------------------------------
def has_pair_bruteforce(nums, k):
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            logging.info(f"Checking pair: ({nums[i]}, {nums[j]})")

            if nums[i] + nums[j] == k:
                logging.info(f"Pair found: ({nums[i]}, {nums[j]})")
                return True

    return False


# --------------------------------------------------
# EDGE CASE TESTS
# --------------------------------------------------
def run_tests():
    test_cases = [
        # Basic case
        ([10, 15, 3, 7], 17),

        # No pair
        ([1, 2, 3, 4], 10),

        # Duplicate numbers (valid case)
        ([5, 5], 10),

        # Duplicate numbers (invalid case)
        ([5], 10),

        # Negative numbers
        ([-1, -2, -3, -4, 5], 1),

        # Mixed positive/negative
        ([3, -1, 9, 8, 2], 7),

        # Zero handling
        ([0, 4, 3, 0], 0),

        # Empty list
        ([], 5),

        # Single element
        ([10], 10),

        # Large numbers
        ([1000000, 500000, -500000], 500000),
    ]

    methods = [
        ("One Pass", has_pair_one_pass),
        ("Two Pass", has_pair_two_pass),
        ("Two Pointers", has_pair_two_pointers),
        ("Brute Force", has_pair_bruteforce),
    ]

    for nums, k in test_cases:
        print("\n" + "=" * 50)
        print(f"Input: nums={nums}, k={k}")

        for name, method in methods:
            logging.info(f"Running {name}")
            result = method(nums, k)
            print(f"{name}: {result}")


# --------------------------------------------------
# MAIN
# --------------------------------------------------
def main():
    run_tests()


if __name__ == "__main__":
    main()


