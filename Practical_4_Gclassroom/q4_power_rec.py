def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        x, n = 1/x, -n
    half = power(x, n // 2)
    return half * half if n % 2 == 0 else half * half * x

if __name__ == "__main__":
    result = power(2, 3)
    print(f"2^3: {result}")