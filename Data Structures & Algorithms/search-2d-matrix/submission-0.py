class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a=[]
        for x in matrix:
            for y in x:
                a.append(y)
        print(a)
        left=0
        right=len(a)-1
        while left<=right:
            mid= left+(right-left)//2
            if a[mid]==target:
                return True
            elif a[mid]<target:
                left=mid+1
                
            else:
                right=mid-1
        return False