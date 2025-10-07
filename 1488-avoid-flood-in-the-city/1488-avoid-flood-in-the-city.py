class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        res = [-1] * n

        hash = {}
        dryDays = []

        for i in range(0, n):
            if rains[i] == 0:
                dryDays.append(i)
            else:
                lake = rains[i]
                if lake in hash:
                    j=0
                    while j < len(dryDays) and dryDays[j] < hash[lake] - 1:
                        j += 1

                    if j >= len(dryDays): 
                        return []
                    else:
                        res[dryDays[j]] = lake
                        # dryDays.erase(dryDays.begin()+j)
                        dryDays.remove(dryDays[j])
                        hash[lake] = i+1
                else:
                    hash[lake] = i+1
                
        for i in range(0, n):
            if rains[i] == 0 and res[i] == -1:
                res[i] = 1
        return res