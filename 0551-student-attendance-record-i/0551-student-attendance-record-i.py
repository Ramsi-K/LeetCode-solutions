class Solution:
    def checkRecord(self, s: str) -> bool:
        counter = Counter(s)
        if counter.get("A", 0) < 2:
            if counter.get("L", 0) < 3: return True
            else: 
                # out = [True for i in range(len(s)-2) if s[i:i+3] == "LLL"]
                # if out : return False
                # else: return True
                # print(out)
                for i in range(len(s) - 2):
                    if s[i:i+3] == "LLL":
                        return False
                return True
        return False


        