class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # initialize stack
        stack = []
        # for item in tokens:
        for i in tokens:
            # if item is a +
            if i == '+':
                # append stack.pop() + stack.pop()
                stack.append(stack.pop() + stack.pop())
            # elif item is -:
            elif i == '-':
                # define a, b variable for order
                a, b = stack.pop(), stack.pop()
                # substract a to b
                stack.append(b-a)
            # elif item is *:
            elif i == '*':
                # append stack.pop() * stack.pop() to the stack
                stack.append(stack.pop() * stack.pop())
            # elif item is /:
            elif i == '/':
                # define a, b for order
                a, b = stack.pop(), stack.pop()
                # append int(b/a)
                stack.append(int(b/a))
            # else append item to stack
            else:
                stack.append(int(i))
        # return top of the stack
        return stack[-1]
        