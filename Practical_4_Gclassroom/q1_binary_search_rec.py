def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    result = binary_search(arr, 7, 0, len(arr) - 1)
    print(f"Index of 7: {result}")