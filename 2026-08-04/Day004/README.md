# Problem Name: Design Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `push(val)` pushes the element `val` onto the stack.
- `pop()` removes the element on the top of the stack.
- `top()` gets the top element of the stack.
- `getMin()` retrieves the minimum element in the stack.

You must implement a solution with $O(1)$ time complexity for each function.

## Sample Input
```python
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin() # returns -3
minStack.pop()
minStack.top()    # returns 0
minStack.getMin() # returns -2
```

## Sample Output
```python
# Sequential outputs from getMin, pop, top, getMin:
-3, None, 0, -2
```

## Explanation
- When `-2`, `0`, and `-3` are pushed, the minimum element in the stack is `-3`.
- After calling `pop()`, the top element `-3` is removed. The elements remaining are `[-2, 0]`.
- The top element is now `0`, and the minimum element is `-2`.

---

## Approach
To achieve $O(1)$ time complexity for `getMin()`, we cannot traverse the stack. We must keep track of the minimums dynamically as elements are pushed and popped. We can use the **Two Stacks Approach**:
1. **Primary Stack (`stack`)**: Stores all the elements normally.
2. **Min Stack (`min_stack`)**: Stores the minimum values. The top of `min_stack` will always represent the minimum value present in `stack` at the current height.
   - **`push(val)`**: Push `val` to `stack`. If `min_stack` is empty or `val` is less than or equal to the current minimum (the top of `min_stack`), we push `val` to `min_stack`.
   - **`pop()`**: Pop the top element from `stack`. If the popped element equals the top of `min_stack`, we also pop it from `min_stack`.
   - **`top()`**: Return the top element of `stack` without modifying it.
   - **`getMin()`**: Return the top element of `min_stack`.

## Time Complexity
- **Time Complexity:** $O(1)$ for `push`, `pop`, `top`, and `getMin` because we only perform basic push/pop/peek operations on Python lists.

## Space Complexity
- **Space Complexity:** $O(N)$ where $N$ is the number of elements pushed, as we may store up to $N$ elements in both the primary and min stacks.
