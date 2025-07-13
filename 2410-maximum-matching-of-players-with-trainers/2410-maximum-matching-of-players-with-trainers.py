class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        m, n = len(players), len(trainers)
        count = 0
        i = j = 0

        while i < m and j < n:
            if players[i] <= trainers[j]:
                # Match found
                count += 1
                i += 1
                j += 1
            else:
                # Try next trainer
                j += 1

        return count