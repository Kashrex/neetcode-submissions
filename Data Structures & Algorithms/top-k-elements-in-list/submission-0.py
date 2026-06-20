class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicti={}
        listi=list()
        for x in nums:
            if x in dicti:
                dicti[x]+=1
            else:
                dicti[x]=1
        sorted_descending = dict(sorted(dicti.items(), key=lambda item: item[1], reverse=True))
        print(sorted_descending)
        for key,value in list(sorted_descending.items())[:k]:
            listi.append(key)

        return listi