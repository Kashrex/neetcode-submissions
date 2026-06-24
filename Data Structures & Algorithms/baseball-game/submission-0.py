class Solution:
    def calPoints(self, operations: List[str]) -> int:
        topo = []

        for x in range(len(operations)):
            if operations[x] not in ["+", "D", "C"]:
                topo.append(int(operations[x]))

            elif operations[x] == "+":
                topo.append(topo[-1] + topo[-2])

            elif operations[x] == "D":
                topo.append(topo[-1] * 2)

            elif operations[x] == "C":
                topo.pop()

        return sum(topo)