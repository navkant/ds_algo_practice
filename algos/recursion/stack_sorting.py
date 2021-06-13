# standard library imports here


# third party imports here


# internal imports here


class Stack:
    def __init__(self, stack=list()):
        self.stack = stack

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) != 0:
            top = self.stack[-1]
            self.stack = self.stack[:-1]
            return top
        else:
            raise IndexError('Stack empty')

    def sort_stack(self):
        if len(self.stack) == 1:
            return self.stack
        else:
            pass
        top = self.pop()
        self.stack = self.sort_stack()
        self.stack = self.put_element_in_stack(top)
        return self.stack

    def put_element_in_stack(self, val):
        if len(self.stack) == 0 or self.stack[-1] <= val:
            self.push(val)
            return self.stack

        top = self.pop()
        # self.stack = self.stack[:-1]
        self.stack = self.put_element_in_stack(val)
        self.push(top)
        return self.stack


if __name__ == '__main__':
    obj = Stack([9, 8, 7, 6, 5, 4, 3])
    obj.sort_stack()
    print(obj.stack)