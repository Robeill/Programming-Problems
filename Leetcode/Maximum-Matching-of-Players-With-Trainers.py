class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        j = 0
        count = 0
        for i in range(len(players)):
            while j < len(trainers) and trainers[j] < players[i]:
                j += 1
            if j < len(trainers):
                count += 1
                j += 1
        return count
