class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dicti={}
        # for x in s:
        #     if x in dicti:
        #         dicti[x]+=1
        #     else:
        #         dicti[x]=1
        # for x in t:
        #     if x in dicti:
        # return len(set(s))==len(set(t))

        s,t=list(s),list(t)
        s.sort(),t.sort()
        return s==t