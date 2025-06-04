class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        m=len(word)-numFriends+1 # splits to be done with m length 
        if numFriends==1: # if only one split we can do total word is taken 
            return word

        return max(word[i:i+m] for i in range(len(word)))