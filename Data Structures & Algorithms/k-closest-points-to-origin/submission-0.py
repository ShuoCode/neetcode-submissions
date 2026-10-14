class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        dist = [[(point[0]**2 + point[1]**2), point[0], point[1]] for point in points]
        heapq.heapify(dist)
        
        for i in range(k):
            a = heapq.heappop(dist)
            res.append([a[1], a[2]])
        
        return res