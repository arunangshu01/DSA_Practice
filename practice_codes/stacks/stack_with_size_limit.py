from typing import List


class StackWithSizeLimit:

    def __init__(self, max_size):
        self.list_stack: List[int] = []
        self.max_size = max_size

    def __str__(self):
        if self.list_stack:
            stack_items = [str(stack_item) for stack_item in reversed(self.list_stack)]
            result = "\n".join(stack_items)
            return result
        return "The Stack has been deleted."

    def is_stack_empty(self):
        if self.list_stack == [] or len(self.list_stack) == 0:
            return True
        return False

    def is_stack_full(self):
        if len(self.list_stack) == self.max_size:
            return True
        return False

    def push_element(self, value):
        if self.is_stack_full():
            raise Exception("Size Limit of the Stack is exceeded. So, can't add any new element.")
        self.list_stack.append(value)
        return f"Element Value: {value} is being pushed into the Stack."

    def pop_element(self):
        if self.is_stack_empty():
            raise Exception("There is no element in the Stack.")
        popped_element = self.list_stack[-1]
        self.list_stack.pop()
        return f"The last element of value: {popped_element} has been popped out of the Stack."

    def peek_element(self):
        if self.is_stack_empty():
            raise Exception("There is no element in the Stack.")
        peeked_element = self.list_stack[-1] or self.list_stack[len(self.list_stack) - 1]
        return f"The last element of the Stack is of value: {peeked_element}."

    def delete_stack(self):
        self.list_stack = None


if __name__ == "__main__":
    try:
        stack_with_size_limit = StackWithSizeLimit(max_size=10)
        print(stack_with_size_limit.push_element(value=10))
        print(stack_with_size_limit.push_element(value=20))
        print(stack_with_size_limit.push_element(value=30))
        print(stack_with_size_limit.push_element(value=40))
        print(stack_with_size_limit.push_element(value=50))
        print(stack_with_size_limit.push_element(value=60))
        print(stack_with_size_limit.push_element(value=70))
        print(stack_with_size_limit.push_element(value=80))
        print(stack_with_size_limit.push_element(value=90))
        print(stack_with_size_limit.push_element(value=100))
        # print(stack_with_size_limit.push_element(110))

        # stack_with_size_limit.delete_stack()
        # print(stack_with_size_limit)

        print(stack_with_size_limit)

        print(stack_with_size_limit.peek_element())
        print(stack_with_size_limit.pop_element())
        print(stack_with_size_limit)

        print(stack_with_size_limit.peek_element())
        print(stack_with_size_limit.pop_element())
        print(stack_with_size_limit)

        print(stack_with_size_limit.peek_element())
        print(stack_with_size_limit.pop_element())
        print(stack_with_size_limit)

        print(stack_with_size_limit.peek_element())
        print(stack_with_size_limit.pop_element())
        print(stack_with_size_limit)

        print(stack_with_size_limit.peek_element())
        print(stack_with_size_limit.pop_element())
        print(stack_with_size_limit)

        print(stack_with_size_limit.peek_element())
        print(stack_with_size_limit.pop_element())
        print(stack_with_size_limit)

        print(stack_with_size_limit.peek_element())
        print(stack_with_size_limit.pop_element())
        print(stack_with_size_limit)

        print(stack_with_size_limit.peek_element())
        print(stack_with_size_limit.pop_element())
        print(stack_with_size_limit)

        print(stack_with_size_limit.peek_element())
        print(stack_with_size_limit.pop_element())
        print(stack_with_size_limit)

        print(stack_with_size_limit.peek_element())
        print(stack_with_size_limit.pop_element())
        print(stack_with_size_limit)

        print(stack_with_size_limit.peek_element())
        print(stack_with_size_limit.pop_element())
        print(stack_with_size_limit)

    except Exception as e:
        print(e.__str__())
