class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for op in operations:
            if op.isnumeric() or op.startswith("-"):
                scores.append(int(op))
            elif op == "+":
                n1, n2 = scores[-1], scores[-2]
                scores.append(n1 + n2)
            elif op == "C":
                scores.pop()
            elif op == "D":
                n = scores[-1]
                scores.append(n * 2)

        return sum(scores)