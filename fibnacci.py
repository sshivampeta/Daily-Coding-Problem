def fib(n: int) -> int:
    """
    Return the nth Fibonacci number using O(1) space.

    :param n: Index (0-based)
    :return: Fibonacci number at index n
    :raises ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, curr = 0, 1

    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr  # shift window

    return curr


if __name__ == "__main__":
    for i in range(10):
        print(f"fib({i}) = {fib(i)}")