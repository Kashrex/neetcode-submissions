class Solution:
    def isPalindrome(self, s: str) -> bool:
        popo=[]
        for x in s:
            if x.isalnum():
                popo.append(x.lower())
        return True if popo==list(reversed(popo)) else False