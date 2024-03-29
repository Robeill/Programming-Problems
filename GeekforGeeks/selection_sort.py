class Solution:
    def select(self, arr, i):
    # code here 
        min_index = i
    def selectionSort(self, arr, n):
    # code here
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[min_index], arr[i] = arr[i], arr[min_index]
        return arr