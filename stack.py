
from collections import deque
#stack = deque()

#print(dir(stack))

#print(stack.__dir__())

#print(dict(stack))

#stack.append("hello")
#stack.append("world")

#stack.pop()

#print(stack)


class Stack():
    def __init__(self):
        self.container = deque()
    
    def push(self, val):
        self.container.append(val)
       
    def pop(self):
        return self.container.pop()
       
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
        
    def size(self):
        return len(self.container)
        
#stack = Stack()
#stack.push(1)
#stack.push(2)
#stack.push(3)
#stack.push(4)
#stack.push(5)
#print(stack.peek())
#print(stack.is_empty())
#print(stack.size())
#print(stack.pop())
#print(stack.peek())
#print(stack.size())


#practice
def is_matched(ch1, ch2):
    match_dict = {
    ")":"(",
    "}":"{",
    "]":"["
    }
    
    return match_dict[ch1] == ch2

def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=="{" or ch=="[":
            stack.push(ch)
        if ch==")" or ch=="}" or ch=="]":
            if stack.size() == 0:
                return False
            if not is_matched(ch,stack.pop()):
                return False
        
    return stack.size() == 0
    


if __name__ == "__main__":
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))