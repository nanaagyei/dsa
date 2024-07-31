
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
            return self.data[0]
        else:
            return None


class Queue:
    """
    Creates the queue data structure.
    """

    def __init__(self):
        self.data = []

    def enqueue(self, element):

        """
        Adds an element to the end of the queue.

        Parameters:
            element (Any): The element to be added to the queue.

        Returns:
            None
        """

        return self.data.append(element)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)
        else:
            return None
    
    def read(self):
        """
        Returns the first element of the data list.

        Returns:
            The first element of the data list if it exists, otherwise None.
        """
        if self.data:
            return self.data[0]
        else:
            return None


class CircularQueue():
    """
    Creates a circular queue
    """

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size # create an array (queue) of length, size
        self.head = self.tail = -1 # initialize head and tail indices to -1 if queue is empty
        
    def enqueue(self, data):
        """
        Enqueues the given data into the circular queue.

        Parameters:
            data (Any): The data to be enqueued.

        Returns:
            None
        """
        if (self.tail + 1) % self.size == self.head:
            print("Queue is full\n")
        else:
            if self.head == -1:
                self.head = 0
            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = data
    
    def dequeue(self):
        """
        Dequeues an element from the circular queue.

        Returns:
            Any: The dequeued element if the queue is not empty, None otherwise.

        Raises:
            None
        """
        if self.head == -1:
            print("Queue is empty\n")
        else:
            data = self.queue[self.head]
            if self.head == self.tail: # last/only element in the queue
                self.head = self.tail = -1
            else:
                self.head = (self.head + 1) % self.size # increase the head index circularly
            return data

    def print_queue(self):
        """
        Prints the elements of the circular queue.

        Returns:
            None
        """
        if self.head == -1:
            print("Queue is empty\n")
        else:
            i = self.head
            while True:
                print(self.queue[i], end = " ")
                i = (i + 1) % self.size
                if i == self.tail:
                    break

#########################################################################################
# Using the stack class in a real world code
class Linter:

    def __init__(self):

        """
        Initializes a new instance of the Linter class.

        This constructor creates a new instance of the Linter class and initializes its 'stack' attribute
        with a new instance of the Stack class.

        Parameters:
            None

        Returns:
            None
        """
        self.stack = Stack()

    def lint(self, text):
        """
        Checks the given text for balanced opening and closing braces.

        Parameters:
            text (str): The text to be checked.

        Returns:
            Union[bool, str]: True if the text has balanced braces, otherwise a string indicating the mismatched or missing brace.
        """
        for char in text:
            if self.is_opening_brace(char):
                self.stack.push(char)
            elif self.is_closing_brace(char):
                print(f"Current elements in stack: {self.stack.data}")
                popped_opening_brace = self.stack.pop()
                if not popped_opening_brace:
                    return f"{char} doesn't have an opening brace"
                if self.is_not_match(popped_opening_brace, char):
                    return f"{char} has mismatched opening brace"
                print(f"Updated stack: {self.stack.data}")
        if self.stack.read():
            return f"{self.stack.read()} does not have closing brace"
        return True
    
    def is_opening_brace(self, char):
        """
        Check if the given character is an opening brace.

        Parameters:
            char (str): The character to be checked.

        Returns:
            bool: True if the character is an opening brace, False otherwise.
        """
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
print(linter.lint("( x = (y:[1, 2, 3]))"))
