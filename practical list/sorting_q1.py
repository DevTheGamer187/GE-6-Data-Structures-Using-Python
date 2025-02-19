def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
    print("Sorted array is:", arr)
            
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("Sorted array is:", arr)
                
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j] :
                min_idx = j
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("Sorted array is:", arr)
                
l1 = []

while True:
    val = int(input("enter element:- "))
    l1.append(val)
    terminate = input("want to terminate? press y otherwise press any key and enter:- ")
    if terminate == "y":
        break
print("List is : " , l1)
print("SORTING TECHINQUE")
print("Press 1 for Insertion Sort")
print("Press 2 for Binary Sort")
print("Press 3 for Selection Sort")
choice = int(input("Enter Your Choice :- "))
if choice == 1:
    insertionSort(l1)
elif choice == 2:
    bubbleSort(l1)
elif choice == 3:
    selectionSort(l1)
else:
    print("enter Correct Choice")

