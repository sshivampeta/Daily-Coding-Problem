import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


# --------------------------------------------------
# 1. USING DIVISION (WITH ZERO HANDLING)
# --------------------------------------------------
def product_with_division(nums):
    logging.info(f"Input: {nums}")

    n = len(nums)
    if n == 0:
        return []

    total_product = 1
    zero_count = 0

    # Calculate product of non-zero elements
    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            total_product *= num

    logging.info(f"Total product (non-zero): {total_product}, zeros: {zero_count}")

    result = []

    for num in nums:
        if zero_count > 1:
            result.append(0)
        elif zero_count == 1:
            if num == 0:
                result.append(total_product)
            else:
                result.append(0)
        else:git
            result.append(total_product // num)

    return result


# --------------------------------------------------
# 2. PREFIX + SUFFIX ARRAYS (NO DIVISION)
# --------------------------------------------------
def product_prefix_suffix(nums):
    logging.info(f"Input: {nums}")

    n = len(nums)
    if n == 0:
        return []

    prefix = [1] * n
    suffix = [1] * n
    result = [1] * n

    # Build prefix
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    # Build suffix
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    logging.info(f"Prefix: {prefix}")
    logging.info(f"Suffix: {suffix}")

    # Build result
    for i in range(n):
        result[i] = prefix[i] * suffix[i]

    return result


# --------------------------------------------------
# 3. OPTIMIZED (NO DIVISION, O(1) EXTRA SPACE)
# --------------------------------------------------
def product_optimized(nums):
    logging.info(f"Input: {nums}")

    n = len(nums)
    if n == 0:
        return []

    result = [1] * n

    # Prefix pass
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
        logging.info(f"Prefix step {i}: result={result}")

    # Suffix pass
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
        logging.info(f"Suffix step {i}: result={result}")

    return result


# --------------------------------------------------
# 4. BRUTE FORCE (FOR COMPLETENESS)
# --------------------------------------------------
def product_bruteforce(nums):
    logging.info(f"Input: {nums}")

    n = len(nums)
    result = []

    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= nums[j]
        result.append(prod)

    return result


# --------------------------------------------------
# EDGE CASE TESTS
# --------------------------------------------------
def run_tests():
    test_cases = [
        # Basic
        [1, 2, 3, 4, 5],
        [3, 2, 1],

        # With one zero
        [1, 2, 0, 4],

        # With multiple zeros
        [0, 0, 3, 4],

        # All zeros
        [0, 0, 0],

        # Negative numbers
        [-1, 2, -3, 4],

        # Single element
        [5],

        # Two elements
        [2, 3],

        # Empty
        [],

        # Large numbers
        [100, 200, 300],

        # Mixed
        [1, -1, 0, 2, -2],
    ]

    methods = [
        ("Division", product_with_division),
        ("Prefix-Suffix", product_prefix_suffix),
        ("Optimized", product_optimized),
        ("Brute Force", product_bruteforce),
    ]

    for nums in test_cases:
        print("\n" + "=" * 60)
        print(f"Input: {nums}")

        for name, method in methods:
            logging.info(f"Running {name}")
            result = method(nums)
            print(f"{name}: {result}")


# --------------------------------------------------
# MAIN
# --------------------------------------------------
def main():
    run_tests()


if __name__ == "__main__":
    main()