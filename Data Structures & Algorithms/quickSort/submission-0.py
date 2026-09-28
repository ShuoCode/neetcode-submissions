# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, pairs: List[Pair], s: int, e: int) -> None:
        # Base case
        if e - s + 1 <= 1:
            return

        # Setup
        pivot = pairs[e]
        left = s

        # Partition - Divide
        for i in range(s, e):
            if pairs[i].key < pivot.key:
                tmp = pairs[i]
                pairs[i] = pairs[left]
                pairs[left] = tmp
                left += 1
        
        # Place pivot at correct position
        pairs[e] = pairs[left]
        pairs[left] = pivot

        # Conquer
        self.quickSortHelper(pairs, s, left - 1)
        self.quickSortHelper(pairs, left + 1, e)

        return