class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        pathTable = {}
        for path in paths:
            pathTable[path[0]] = path[1]
        for city in pathTable.values():
            if city not in pathTable.keys():
                return city
            
        