class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = {}  # Track the latest color of each ball
        distinct_colors = set()  # Track unique colors used
        color_count = {}  # Track frequency of each color
        result = []

        for x, y in queries:
            # If ball x already has a color
            if x in ball_colors:
                old_color = ball_colors[x]
                if old_color == y:  # If color is the same, skip redundant updates
                    result.append(len(distinct_colors))
                    continue

                # Reduce count of the old color
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    distinct_colors.remove(old_color)  # Remove if no ball uses it

            # Assign new color
            ball_colors[x] = y
            if y not in color_count:
                color_count[y] = 0
            color_count[y] += 1
            distinct_colors.add(y)  # Add to set of used colors

            # Store the count of distinct colors
            result.append(len(distinct_colors))

        return result


        