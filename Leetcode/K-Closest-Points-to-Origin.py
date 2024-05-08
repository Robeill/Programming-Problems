class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(point, (point[0]**2 + point[1]**2) ** 0.5) for point in points]
        distances.sort(key=lambda x: x[1])
        return [distance[0] for distance in distances[:k]]
