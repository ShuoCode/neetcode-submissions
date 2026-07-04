class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        stackPt = 0
        sum = 0

        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(op))

        sum = 0
        for j in range(len(stack)):
            sum += stack[j]

        return sum