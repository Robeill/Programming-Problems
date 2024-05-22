class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_seen = {}
        min_length = float('inf')
        index = 0
        for card in cards:
            if card in last_seen:
                min_length = min(min_length, index - last_seen[card] + 1)
            last_seen[card] = index
            index += 1
        return min_length if min_length != float('inf') else -1
