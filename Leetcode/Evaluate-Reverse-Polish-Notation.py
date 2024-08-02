class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for nums in tokens:
            if nums == "+":
                stack.append(stack.pop() + stack.pop())
            elif nums == "-":
                second, first = stack.pop(), stack.pop()
                stack.append(first - second)
            elif nums == "*":
                stack.append(stack.pop() * stack.pop())
            elif nums == "/":
                second, first = stack.pop(), stack.pop()
                stack.append(int(first / second))                
            else:
                stack.append(int(nums))
        return stack[0]
