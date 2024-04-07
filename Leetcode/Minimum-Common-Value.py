class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
    # Two pointer Approach
        nums1.sort()
        nums2.sort()
        p1 = 0
        p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return -1
    '''
    # Using the intersection Operator
        common_elements = set(nums1) & set(nums2)
        if common_elements:
            return min(common_elements)  
        else:
            return -1 
    '''
