"""
Day 3: Problem 4 - Design Min Stack (OOP)
Language: Python 3
"""


class MinStack:
    """
    A stack data structure that supports push, pop, top, and retrieving
    the minimum element in O(1) constant time.
    """

    def __init__(self):
        """
        Initializes the stack and min_stack.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """
        Pushes the element val onto the stack.
        """
        self.stack.append(val)
        # Push to min_stack if it's empty or val is less than or equal to current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """
        Removes the element on the top of the stack.
        Raises IndexError if the stack is empty.
        """
        if not self.stack:
            raise IndexError("pop from empty stack")

        val = self.stack.pop()
        # If the popped value is the current minimum, pop it from min_stack too
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        """
        Gets the top element of the stack.
        Raises IndexError if the stack is empty.
        """
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1]

    def getMin(self) -> int:
        """
        Retrieves the minimum element in the stack.
        Raises IndexError if the stack is empty.
        """
        if not self.min_stack:
            raise IndexError("getMin from empty stack")
        return self.min_stack[-1]


if __name__ == "__main__":
    # Test Cases
    print("Initializing MinStack...")
    min_stack = MinStack()

    # Test Case 1: Standard Push and Min check
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)

    assert min_stack.getMin() == -3, f"Expected min to be -3, got {min_stack.getMin()}"
    print("Check 1 passed: Minimum after pushing -2, 0, -3 is -3.")

    # Test Case 2: Pop and Min check
    min_stack.pop()
    assert min_stack.top() == 0, f"Expected top to be 0, got {min_stack.top()}"
    assert min_stack.getMin() == -2, f"Expected min to be -2, got {min_stack.getMin()}"
    print("Check 2 passed: Top is 0, minimum after popping is -2.")

    # Test Case 3: Push duplicate min
    min_stack.push(-2)
    assert min_stack.getMin() == -2, f"Expected min to be -2, got {min_stack.getMin()}"
    min_stack.pop()
    assert min_stack.getMin() == -2, f"Expected min to be -2, got {min_stack.getMin()}"
    print("Check 3 passed: Handled duplicate min values correctly.")

    # Test Case 4: Exception handling for empty stack
    empty_stack = MinStack()
    try:
        empty_stack.pop()
        assert False, "Should have raised IndexError on pop from empty stack"
    except IndexError:
        print("Check 4 passed: Correctly raised IndexError on pop from empty stack.")

    try:
        empty_stack.getMin()
        assert False, "Should have raised IndexError on getMin from empty stack"
    except IndexError:
        print("Check 5 passed: Correctly raised IndexError on getMin from empty stack.")

    print("All sample and edge test cases executed successfully!")
