class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxCandies = max(candies)
        for i, candy in enumerate(candies):
                if extraCandies + candy >= maxCandies:
                        result.append(True)
                else:
                        result.append(False)
        return result

