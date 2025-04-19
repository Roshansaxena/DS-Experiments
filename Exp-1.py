# Python program to insert an element at a specific position in an Array
def insertElement(arr, n, x, pos):
    # shift elements to the right which are on the right side of pos
    for i in range(n - 1, pos - 1, -1):
        arr[i + 1] = arr[i]
    arr[pos] = x

# Driver code
if __name__ == '__main__':
    # Declaring array and space for extra elements (-1 is used as placeholder)
    arr = [2, 4, 1, 8, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    n = 5  # current number of valid elements
    x = 10
    pos = 2

    print("Before insertion:")
    for i in range(n):
        print(arr[i], end=" ")

    insertElement(arr, n, x, pos)
    n += 1

    print("\nAfter insertion:")
    for i in range(n):
        print(arr[i], end=" ")
