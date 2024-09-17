class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = {'U': 0, 'D': 0, 'R': 0, 'L': 0}
        d.update(Counter(moves))
        # u_d, r_l = d['U'] - d['D'], d['R'] - d['L']
        # return u_d == r_l == 0
        return d['U'] == d['D'] and d['R'] == d['L']
