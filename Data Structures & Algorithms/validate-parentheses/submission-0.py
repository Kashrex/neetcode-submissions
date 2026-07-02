# class Solution:
#     def isValid(self, s: str) -> bool:
#         arrO=['(','{','[']
#         arrC=[')','}',']']
#         topa=[]
#         for x in s:
#             if x in arrO:
#                 topa.append(x)
#             elif x in arrC:
#                 e=topa.pop()
#                 if x==e:
#                     continue
#                 else:
#                     return False
#         return True
class Solution:
    def isValid(self, s: str) -> bool:
        arrO = ['(', '{', '[']
        arrC = [')', '}', ']']

        topa = []

        for x in s:
            if x in arrO:
                topa.append(x)

            elif x in arrC:
                if not topa:
                    return False

                e = topa.pop()

                if x == ')' and e != '(':
                    return False
                if x == '}' and e != '{':
                    return False
                if x == ']' and e != '[':
                    return False

        return len(topa) == 0