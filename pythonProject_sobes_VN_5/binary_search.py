"""
Binary Search Algorithm

Given a sorted array `arr` and a target value `x`, this function returns:
- The index of `x` in `arr` if found
- Otherwise, returns -1 (or insertion point as -1 - pos for further use)

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def binarySearch(arr, x):
    # Initialize left and right pointers
    l = 0
    r = len(arr) - 1

    while l <= r:
        # Calculate middle index (avoids overflow compared to (l+r)//2)
        mid = l + (r - l) // 2

        # Element found at midpoint
        if arr[mid] == x:
            return mid

        # If target is in right half, move left pointer
        elif arr[mid] < x:
            l = mid + 1

        # If target is in left half, move right pointer
        else:
            r = mid - 1

    # Element not found (could return -1 - l for insertion point)
    return -1


# Example Usage
if __name__ == "__main__":
    # Sorted array for testing
    test_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23

    print(f"Searching for {target} in array: {test_array}")
    result = binarySearch(test_array, target)

    if result != -1:
        print(f"Element found at index {result} (value = {test_array[result]})")
    else:
        print("Element not found in array")

    # Additional test cases
    print("\nAdditional tests:")
    print(binarySearch(test_array, 5))  # Should return 1
    print(binarySearch(test_array, 100))  # Should return -1
    print(binarySearch([], 42))  # Edge case: empty array