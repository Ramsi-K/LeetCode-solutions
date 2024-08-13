class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        my_dict = {"UP": -n, "DOWN": n, "RIGHT": 1, "LEFT": -1}
        final_pos = sum([my_dict.get(item) for item in commands])
        return final_pos