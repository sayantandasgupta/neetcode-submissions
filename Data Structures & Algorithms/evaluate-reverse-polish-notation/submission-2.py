class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                n1 = stack.pop()
                n2 = stack.pop()
                if token == "+":
                    stack.append(n1 + n2)
                elif token == "-":
                    stack.append(abs(n1 - n2))
                elif token == "*":
                    stack.append(n1 * n2)
                elif token == "/":
                    stack.append(max(n1, n2) // min(n1,n2))
            else:
                stack.append(int(token))

        return stack[-1]