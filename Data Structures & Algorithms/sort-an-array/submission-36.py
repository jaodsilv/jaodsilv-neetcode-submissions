class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(a, b):
            i, j = 0, 0
            res = []
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    res.append(a[i])
                    i += 1
                elif a[i] > b[j]:
                    res.append(b[j])
                    j += 1
                else:
                    res.append(a[i])
                    res.append(b[j])
                    i += 1
                    j += 1
            res.extend(a[i:] + b[j:])
            return res
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            middle = len(arr) // 2
            left = mergeSort(arr[:middle])
            right = mergeSort(arr[middle:])
            return merge(left, right)
        return mergeSort(nums)
