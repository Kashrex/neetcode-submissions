# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         a=asteroids
#         top=a.pop()
#         le=len(a)
#         while a:
#             b = a.pop()
#             if top > 0:
#                 if b > 0:
#                     continue
#                 else:
#                     a.append(b)
#             else:
#                 if top < 0:
#                     continue
#                 else:
#                     a.append(b)
#         return

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack