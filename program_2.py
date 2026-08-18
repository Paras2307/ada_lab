class Sort:

    # Merge Sort
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result += left[i:]
        result += right[j:]

        return result

    # Quick Sort
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[-1]

        left = []
        right = []

        for x in arr[:-1]:
            if x <= pivot:
                left.append(x)
            else:
                right.append(x)

        return self.quick_sort(left) + [pivot] + self.quick_sort(right)


# Taking input from user
arr = list(map(int, input("Enter numbers: ").split()))

s = Sort()

print("Original array:", arr)
print("Merge Sort:", s.merge_sort(arr))
print("Quick Sort:", s.quick_sort(arr))