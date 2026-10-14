class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if a != b:
                heapq.heappush(stones, abs(a - b))

        return abs(stones[0]) if len(stones) > 0 else 0