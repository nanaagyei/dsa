
class Stack:
    """
    Creates the stack data structure. 
    """

    def __init__(self):
        self.data = []
    
    def push(self, element):
        return self.data.append(element)
    
    def pop(self):
        if self.data:
            return self.data.pop()
        else:
            return None
    
    def read(self):
        if self.data:
            return self.data[-1]
        else:
            return None


class Queue:
    """
    Creates the queue data structure.
    """

    def __init__(self):
        self.data = []

    def enqueue(self, element):
        return self.data.append(element)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)
        else:
            return None
    
    def read(self):
        if self.data:
            return self.data[0]
        else:
            return None

#########################################################################################
# Using the stack class in a real world code
class Linter:

    def __init__(self):
        self.stack = Stack()

    def lint(self, text):
        for char in text:
            if self.is_opening_brace(char):
                self.stack.push(char)
            elif self.is_closing_brace(char):
                popped_opening_brace = self.stack.pop()
                if not popped_opening_brace:
                    return f"{char} doesn't have an opening brace"
                if self.is_not_match(popped_opening_brace, char):
                    return f"{char} has mismatched opening brace"
        if self.stack.read():
            return f"{self.stack.read()} does not have closing brace"
        return True
    
    def is_opening_brace(self, char):
        braces = ["(", "{", "["]
        if char in braces:
            return True
        return False

    def is_closing_brace(self, char):
        braces = [")", "}", "]"]
        if char in braces:
            return True
        return False
    
    def is_not_match(self, opening_brace, closing_brace):
        braces_hash = {"(":")", "[":"]", "{":"}"}
        if closing_brace != braces_hash[opening_brace]:
            return True
        return False
#######################################################################################
# Example

linter = Linter()
print(linter.lint("( x = (y:[1, 2, 3))"))