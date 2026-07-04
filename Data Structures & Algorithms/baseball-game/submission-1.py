class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        stackPt = 0

        for i in range(len(operations)):
            if operations[i] == "+":
                stack.append(stack[stackPt] + stack[stackPt-1])
                stackPt += 1
            if operations[i] == "C":
                stack.pop(stack[stackPt])
                stackPt -= 1
            if operations[i] == "D":
                stack.append(stack[stackPt] * 2)
                stackPt += 1
            else:
                stack.append(int(operations[i]))
                stackPt += 1

        for j in range(0, stackPt + 1):
            sum += stack[j]

        return sum