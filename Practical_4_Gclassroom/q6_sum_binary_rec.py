def sum_binary_range(start, end):
    if start > end:
        return 0
    if start == end:
        return start
    mid = (start + end) // 2
    return sum_binary_range(start, mid) + sum_binary_range(mid + 1, end)

def sum_binary(n):
    return sum_binary_range(1, n)

if __name__ == "__main__":
    result = sum_binary(4)
    print(f"Sum of 1 to 4: {result}")