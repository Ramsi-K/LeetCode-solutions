class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Remove punctuation and convert to lowercase
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph.lower())  # Removes non-alphanumeric characters, except spaces

        # Split the paragraph by space and commas
        split_list = paragraph.split(' ')

        # Dictionary to hold word counts
        out = {}
        for word in split_list:
            if word and word not in banned:  # Ensure word isn't empty and not banned
                if word not in out:
                    out[word] = 1
                else:
                    out[word] += 1

        # Get the key with the maximum value
        max_key = max(out, key=out.get)

        return max_key

