class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0       
        j= 0       
        while i <= len(name) and j < len(typed):
            if i < len(name) and typed[j] == name[i]:
                j += 1
                i += 1
            elif typed[j] == name[i-1] and i != 0:
                j += 1
            else:
                return False
        return i == len(name) and j == len(typed)