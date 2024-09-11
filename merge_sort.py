# Merge Sort Algorithm to sort strings by length from longest to shortest
def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point and divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if len(left_half[i]) > len(right_half[j]):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left in the left half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check if any element was left in the right half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Test the modified Merge Sort with three string lists
list1 = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
list2 = ["strawberry", "blueberry", "raspberry", "blackberry", "cranberry", "gooseberry", "mulberry", "boysenberry", "cloudberry", "elderberry"]
list3 = ["pineapple", "mango", "papaya", "guava", "lychee", "jackfruit", "durian", "rambutan", "longan", "soursop"]

# Print original list1
print("Original List 1:", list1)
# Sort list1 using the modified Merge Sort
merge_sort(list1)
# Print sorted list1
print("Sorted List 1:", list1)

# Print original list2
print("\nOriginal List 2:", list2)
# Sort list2 using the modified Merge Sort
merge_sort(list2)
# Print sorted list2
print("Sorted List 2:", list2)

# Print original list3
print("\nOriginal List 3:", list3)
# Sort list3 using the modified Merge Sort
merge_sort(list3)
# Print sorted list3
print("Sorted List 3:", list3)
