class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        requirements = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        requirements.update(Counter(text))

        # Calculate the maximum number of "balloon" words we can form
        # Dividing by the required number for 'l' and 'o' (both needed twice)
        return min(requirements['b'],
                requirements['a'],
                requirements['l'] // 2,
                requirements['o'] // 2,
                requirements['n'])