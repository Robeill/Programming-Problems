class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        res , j = 0 ,0
        for i in range(len(processorTime)):
            res = max(res ,processorTime[i] + tasks[j])
            j += 4
        return res