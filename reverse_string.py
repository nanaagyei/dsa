

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

# Reversing a string using the Stack class.

def reverse_string(text):
    reverse_text = ""
    stack = Stack()
    for char in text:
        stack.push(char)
    
    while stack.read():
        char = stack.pop()
        reverse_text += char
    
    return reverse_text
    


print(reverse_string("abcde"))

# Returns the reverse of a string
def reverse(string):
    if len(string) == 1:
        return string
    else:
        return reverse(string[1:len(string)]) + string[0]

# text = "abcde"
# print(reverse(text))
