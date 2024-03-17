class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        # Mapping of digits to letters
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        combinations = ['']

        for digit in digits:
            # print(f"Digit: {digit}")
            new_combinations = []
            for combination in combinations:
                # print(f"Combination: {combination}, Combinations: {combinations}")
                for letter in digit_map[digit]:
                    # print(f"Letter: {letter}")
                    # print(f"Appending: {combination + letter}")
                    new_combinations.append(combination + letter)
            combinations = new_combinations

        return combinations