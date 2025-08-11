from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from pathlib import Path


def parse_input() -> str:
    with open(Path(__file__).parent.as_posix() + "/" + "input.txt", "r") as file:
        return file.read()


class ParserState(Enum):
    IDLE = "idle"
    OPERATION = "operation"
    LEFT = "left"
    RIGHT = "right"
    READY = "ready"
    FAILED = "failed"


class Operation(ABC):
    type: str = NotImplemented
    state: ParserState = ParserState.LEFT

    def __repr__(self):
        return f"[{self.type}] {self.state}"

    def consume(self, char: str) -> Operation | None:
        if self.state == ParserState.LEFT and char == ")":
            self.state = ParserState.READY
            return self
        else:
            pass


class MultOperation(Operation):
    type = "mul"

    left: int | None = None
    right: int | None = None
    arg: list[str] = []

    state: ParserState = ParserState.LEFT

    def __repr__(self):
        return f"MULT - State {self.state} | Args: ({self.left}, {self.right})"

    def restart(self):
        self.left = None
        self.right = None
        self.arg.clear()
        self.state = ParserState.FAILED

    def consume(self, char: str) -> Operation | None:
        if self.state == ParserState.LEFT:
            if char.isdigit():
                self.arg.append(char)
            elif char == "," and len(self.arg) > 0:
                number_as_str = int("".join(self.arg))
                self.left = number_as_str
                self.state = ParserState.RIGHT
                self.arg.clear()
            else:
                return self.restart()

        elif self.state == ParserState.RIGHT:
            if char.isdigit():
                self.arg.append(char)
            elif char == ")" and len(self.arg) > 0:
                number_as_str = int("".join(self.arg))
                self.right = number_as_str
                self.arg.clear()
                self.state = ParserState.READY

                return self
            else:
                return self.restart()
        else:
            self.state = ParserState.FAILED
            return self


class DoOperation(Operation):
    type = "do"


class DontOperation(Operation):
    type = "don't"


class Parser:
    stack: list[str] = []
    operation: Operation | None = None
    state: ParserState = ParserState.IDLE

    debug: bool = False

    operations: list[Operation] = []

    def __init__(self, operations: list[Operation], debug=False):
        self.operations = operations
        self.debug = debug
        pass

    def restart(self):
        if self.debug:
            print()

        self.state = ParserState.IDLE
        self.stack.clear()
        self.operation = None

    def __repr__(self):
        return f"State {self.state} | Operation ({self.operation}) | Stack {self.stack}"

    def consume(self, char: str) -> MultOperation | None:
        if self.debug:
            print(char, self)

        if self.state == ParserState.IDLE:
            self.stack.append(char)

            if char != "(":
                return

            for operation in self.operations:
                length = len(operation.type)

                phrase = "".join(self.stack[-length - 1 : -1 :])

                if phrase == operation.type:
                    self.restart()
                    self.state = ParserState.OPERATION
                    self.operation = operation()

                    return

        elif self.state == ParserState.OPERATION:
            if not self.operation:
                return

            res = self.operation.consume(char)

            if not res:
                return

            if res.state == ParserState.READY:
                self.restart()
                return res
            else:
                self.restart()


def solution_1(stream: str):
    operations: list[MultOperation] = []
    parser = Parser(operations=[MultOperation], debug=False)

    for char in stream:
        res = parser.consume(char)

        if res is None:
            continue

        operations.append(res)

    total = 0

    for op in operations:
        if op.type == MultOperation.type:
            total += op.left * op.right

    return total, operations


def solution_2(stream: str):
    operations: list[Operation] = []
    parser = Parser(operations=[MultOperation, DoOperation, DontOperation], debug=False)

    for char in stream:
        res = parser.consume(char)

        if res is not None:
            operations.append(res)

    total = 0
    is_enabled = True

    for op in operations:
        if op.type == DoOperation.type:
            is_enabled = True
        elif op.type == DontOperation.type:
            is_enabled = False
        elif op.type == MultOperation.type and is_enabled:
            total += op.left * op.right

    return total, operations


if __name__ == "__main__":
    inp = parse_input()

    total_1, operations_1 = solution_1(inp)

    print(f"Part one: {total_1}")

    total_2, operations_2 = solution_2(inp)

    print(f"Part two: {total_2}")
