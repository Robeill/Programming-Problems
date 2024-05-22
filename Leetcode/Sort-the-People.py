class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heights_dict = zip(heights, names)
        res = sorted(heights_dict, reverse=True)
        return [name for height, name in res]