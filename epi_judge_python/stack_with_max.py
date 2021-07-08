import collections
import sys

from test_framework import generic_test
from test_framework.test_failure import TestFailure

MaxFrequency = collections.namedtuple("MaxFrequency", ("max", "frequency"))


class Stack:
    def __init__(self):
        self.stack = []
        self.maxs_stack = []

    def empty(self) -> bool:
        return len(self.stack) == 0

    def max(self) -> int:
        if not self.empty():
            return self.maxs_stack[-1].max

        return -sys.maxsize - 1

    def _pop_max_frequency(self) -> int:
        return self.maxs_stack.pop()

    def pop(self) -> int:
        if self.empty():
            return None

        popped_item = self.stack.pop()

        if popped_item == self.max():

            max_freq = self._pop_max_frequency()

            if max_freq.frequency > 1:
                self.maxs_stack.append(
                    MaxFrequency(max_freq.max, max_freq.frequency - 1)
                )

        return popped_item

    def push(self, x: int) -> None:
        if x > self.max():
            self.maxs_stack.append(MaxFrequency(x, 1))
        elif x == self.max():
            max_freq = self._pop_max_frequency()
            self.maxs_stack.append(MaxFrequency(max_freq.max, max_freq.frequency + 1))

        return self.stack.append(x)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == "Stack":
                s = Stack()
            elif op == "push":
                s.push(arg)
            elif op == "pop":
                result = s.pop()

                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "max":
                result = s.max()

                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "empty":
                result = int(s.empty())

                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result)
                    )
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure("Unexpected IndexError exception")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "stack_with_max.py", "stack_with_max.tsv", stack_tester
        )
    )
