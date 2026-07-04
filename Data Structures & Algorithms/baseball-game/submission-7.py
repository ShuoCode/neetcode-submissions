class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        stackPt = 0
        sum = 0

        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
                sum += stack[-1]
            elif op == "C":
                sum -= stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
                sum += stack[-1]
            else:
                stack.append(int(op))
                sum += stack[-1]

        return sum