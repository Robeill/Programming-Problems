class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        cust = 0
        max_satisfied = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                cust+=customers[i]
        max_satisfied = max(max_satisfied,cust)
        i = 0
        j = 0
        while j<=minutes-1:
            if grumpy[j] == 1:
                cust+=customers[j]
            j+=1
        max_satisfied = max(max_satisfied,cust)
        if grumpy[i] == 1:
            cust-=customers[i]
        i+=1
        while j<len(grumpy):
            if grumpy[j] == 1:
                cust+=customers[j]
                max_satisfied = max(max_satisfied,cust)
            if grumpy[i] ==1:
                cust-=customers[i]
            i+=1
            j+=1
        return max_satisfied