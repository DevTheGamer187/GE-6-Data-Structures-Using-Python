def sum_linear(n):
    return 0 if n <= 0 else n + sum_linear(n - 1)

if __name__ == "__main__":
    result = sum_linear(4)
    print(f"Sum of 1 to 4: {result}")