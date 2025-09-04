class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        person_one = abs(x-z)
        person_two = abs(y-z)
        if person_one == person_two: return 0
        else: return 1 if person_one<person_two else 2