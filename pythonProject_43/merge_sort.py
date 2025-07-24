def merge(arr1, arr2):
    merged = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i = i + 1
        else:
            merged.append(arr2[j])
            j = j + 1

    while i < len(arr1):
        merged.append(arr1[i])
        i = i + 1

    while j < len(arr2):
        merged.append(arr2[j])
        j = j + 1

    return merged

def merge_sort(arr):

    if len(arr) < 2:
        return arr

    m = len(arr) // 2

    return merge(merge_sort(arr[:m]), merge_sort(arr[m:]))


if __name__ == '__main__':
    arr1 = [3,4]
    arr2 = [1,2]
    arr = [4,1,9,3,5,0]

    print(merge(arr1, arr2))
    print(merge_sort(arr))

# rep5