# Python program to delete an element from an unsorted array

# Driver code
if __name__ == '__main__':
    # Declaring array and key to delete
    arr = [10, 50, 30, 40, 20]
    key = 30

    print("Array before deletion:")
    print(arr)

    # Deletes key if found in the array
    arr.remove(key)

    print("Array after deletion:")
    print(arr)
