def insertion_sort(arr):
    arr_copy = arr.copy()
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and key < arr_copy[j]:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
    return arr_copy

def selection_sort(arr):
    arr_copy = arr.copy()
    for i in range(len(arr_copy)):
        min_idx = i
        for j in range(i + 1, len(arr_copy)):
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
    return arr_copy

def bubble_sort(arr):
    arr_copy = arr.copy()
    n = len(arr_copy)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        if not swapped:
            break
    return arr_copy

def main():
    while True:
        print("\nMenu:")
        print("1. Insertion Sort")
        print("2. Selection Sort")
        print("3. Bubble Sort")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '4':
            print("Exiting the program.")
            break
        elif choice in ('1', '2', '3'):
            try:
                numbers_input = input("Enter numbers separated by spaces: ")
                numbers = list(map(int, numbers_input.split()))
            except ValueError:
                print("Invalid input. Please enter integers only.")
                continue
            
            if choice == '1':
                sorted_numbers = insertion_sort(numbers)
                print("Sorted array using Insertion Sort:", sorted_numbers)
            elif choice == '2':
                sorted_numbers = selection_sort(numbers)
                print("Sorted array using Selection Sort:", sorted_numbers)
            elif choice == '3':
                sorted_numbers = bubble_sort(numbers)
                print("Sorted array using Bubble Sort:", sorted_numbers)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()