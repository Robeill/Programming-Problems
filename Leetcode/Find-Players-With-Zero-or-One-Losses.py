class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        losses = collections.Counter()
        for winner, loser in matches:
            losses[loser] += 1
            players.add(winner)
            players.add(loser)

        no_L , one_L = [], []
        for player in players:
            if losses[player] == 0:
                no_L.append(player)
            elif losses[player] == 1:
                one_L.append(player)
        return [sorted(no_L), sorted(one_L)]