# Notes - Day 3, Problem 4: OOP Design & Min Stack

## Concepts Learned
1. **Auxiliary Data Structures**:
   - Using a second stack (`min_stack`) allows us to preserve history. As elements are added/removed, we maintain the "minimum-so-far" state in sync with the primary stack.
2. **Encapsulation (OOP)**:
   - Defining properties (`self.stack`, `self.min_stack`) and methods (`push`, `pop`, etc.) within a class encapsulates the state and behavior of the stack.
3. **Handling Exceptions**:
   - Raising standard exceptions like `IndexError` when client code attempts invalid operations (like popping from an empty stack) makes the class robust and user-friendly.

## Common Mistakes
- **Neglecting duplicate minimums**: Only pushing to `min_stack` if the pushed value is strictly less than the top of `min_stack` (i.e. `val < self.min_stack[-1]`). If the same minimum value is pushed multiple times (e.g. `push(2)`, `push(2)`), and then popped once, the `min_stack` would incorrectly pop the only reference, leaving no minimum or an outdated one.
- **Linear search in `getMin`**: Calling Python's built-in `min(self.stack)` in `getMin()`. This is an $O(N)$ operation, violating the constant time $O(1)$ requirement.
- **Index Errors**: Forgetting to check if `min_stack` is empty before accessing its top element (`self.min_stack[-1]`), causing runtime crash.

## Alternative Solution
### Stack of Pairs/Tuples
Instead of using two separate stacks, we can store pairs of `(value, minimum_so_far)` on a single stack. This reduces the number of lists we manage.
```python
class MinStackAlternative:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        if not self.stack:
            raise IndexError("pop from empty stack")
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            raise IndexError("getMin from empty stack")
        return self.stack[-1][1]
```
- **Time Complexity:** $O(1)$ for all operations.
- **Space Complexity:** $O(N)$ (stores 2 items per push on the stack).

## Interview Tips
- **Discuss Space vs. Cleanliness**: Compare the two approaches (two stacks vs. one stack of tuples). Storing tuples uses a single stack, which is easier to write, but if the minimum rarely changes, using a separate `min_stack` (and only pushing duplicates/smaller values) might use slightly less memory in practice.
- **Edge cases first**: Always ask or state what happens if `pop()`, `top()`, or `getMin()` is called on an empty stack (throw an exception or return a default/None?).
