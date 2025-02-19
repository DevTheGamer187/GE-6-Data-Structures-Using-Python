def linearSearch(arr, searchValue):
    for i in range(0,len(arr)):
        if arr[i] == searchValue:
            return i
    return None

def binarySearch(arr, searchValue):
    arr.sort()
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == searchValue:
            return mid
        elif searchValue < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None

l1 = []

while True:
    val = int(input("enter element:- "))
    l1.append(val)
    terminate = input("want to terminate? press y otherwise press any key and enter:- ")
    if terminate == "y":
        break
print("List is : " , l1)
print("SEARCHING TECHINQUE")
print("Press 1 for Linear Search")
print("Press 2 for Binary Search")
choice = int(input("Enter Your Choice :- "))
searchValue = eval(input("enter the value to be searched:- "))
if choice == 1:
    print(searchValue, "found at index", linearSearch(l1,searchValue))
elif choice == 2:
    print(searchValue, "found at index", binarySearch(l1,searchValue))
else:
    print("enter Correct Choice")