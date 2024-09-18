class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp_word = ''.join(x.lower() for x in licensePlate if x.isalpha())
        counts = Counter(lp_word)
        keys = set(counts.keys())
        out = []
        print("Counts ", counts)

        for word in words:
            cnts = Counter(word)
            print("WORD: ", word)
            print("CNTS: ", cnts)
            keys_to_remove = set(cnts.keys()) - keys
            print("KEYSTOREMOVE: ", keys_to_remove)

            for key in keys_to_remove:
                del cnts[key]
                print("CNTS: ", cnts)
            if cnts.keys() == counts.keys():
                if all(cnts[k] >= counts[k] for k in cnts.keys()):                
                    out.append(word)
        print(out)

        return min(out, key=len) if out else 0
