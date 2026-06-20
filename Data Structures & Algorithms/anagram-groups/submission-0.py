class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        for words in strs:
            hkey=''.join(sorted(words))
            if hkey not in map:
                map[hkey]=[]
            map[hkey].append(words)
        return list(map.values())