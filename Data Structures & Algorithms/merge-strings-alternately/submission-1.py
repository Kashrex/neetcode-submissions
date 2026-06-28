class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x,y=len(word1),len(word2)
        output=[]
        if x>y:
            for i in range(y):
                output.append(word1[i])
                output.append(word2[i])
                
            output.append(word1[y:])
        else:
            for i in range(x):
                output.append(word1[i])
                output.append(word2[i])
                
            output.append(word2[x:])
        return "".join(output)