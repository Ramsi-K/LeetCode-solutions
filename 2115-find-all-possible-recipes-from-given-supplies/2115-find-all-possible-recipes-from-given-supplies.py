class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = {}
        graph = defaultdict(list)
        available = set(supplies)

        # Build graph and indegree count
        for i, recipe in enumerate(recipes):
            indegree[recipe] = 0
            for ing in ingredients[i]:
                if ing not in available:
                    graph[ing].append(recipe)
                    indegree[recipe] += 1

        # Queue starts with all recipes that have zero indegree (all ingredients available)
        queue = deque()
        for i, recipe in enumerate(recipes):
            if indegree[recipe] == 0:
                queue.append(recipe)

        result = []

        while queue:
            curr = queue.popleft()
            result.append(curr)
            available.add(curr)  # This recipe can now be used as an ingredient

            for nei in graph[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return result