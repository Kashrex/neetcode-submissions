# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         seti=('+','-','*','/')
#         sc=[]
#         ans=0
#         # sd=[]
#         # for x in tokens:
#         #     if x in seti:
#         #         sc.append()
#         #     else:
#         #         sd.append()
#         # for x in sd:
#         #     while len(sd) >= 0:
#         for token in tokens:
#             if token in seti:
#                 a=sc.pop()
#                 b=sc.pop()
#                 sc.append(atokenb)
#             else:
#                 sc.append(token)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]