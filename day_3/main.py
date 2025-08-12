from __future__ import annotations
from abc import ABC
from enum import Enum
from pathlib import Path


def parse_input() -> str:
    with open(Path(__file__).parent.as_posix() + "/" + "input.txt", "r") as file:
        return file.read()


class ParserState(Enum):
    IDLE = "idle"
    OPERATION = "operation"
    PARAMETERS = "parameters"
    READY = "ready"
    FAILED = "failed"


class Operation(ABC):
    type: str = NotImplemented
    state: ParserState = ParserState.PARAMETERS
    args: list[int] = []

    def __init__(self):
        self.args = []

    def __repr__(self):
        return f"[{self.type}] {self.state}"

    def consume(self, char: str) -> Operation | None:
        if self.state == ParserState.PARAMETERS and char == ")":
            self.state = ParserState.READY
            return self


class MultOperation(Operation):
    type = "mul"

    stack: list[str] = []
    state: ParserState = ParserState.PARAMETERS

    def __repr__(self):
        return f"MULT - State {self.state} | Args: {self.args}"

    def restart(self):
        self.stack.clear()
        self.state = ParserState.FAILED

        return self

    def consume(self, char: str) -> Operation | None:
        if self.state != ParserState.PARAMETERS:
            return

        if char.isdigit():
            self.stack.append(char)
        elif char == "," and len(self.stack) > 0:
            number_as_str = int("".join(self.stack))
            self.args.append(number_as_str)
            self.stack.clear()
        elif char == ")" and len(self.stack) > 0:
            number_as_str = int("".join(self.stack))
            self.args.append(number_as_str)
            self.stack.clear()

            if len(self.args) == 2:
                self.state = ParserState.READY
                return self
            else:
                return self.restart()
        else:
            return self.restart()


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

        return self

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

            self.restart()

            if res.state == ParserState.READY:
                return res


def solution_1(stream: str):
    total = 0
    parser = Parser(operations=[MultOperation], debug=False)

    for char in stream:
        res = parser.consume(char)

        if res is None:
            continue

        if res.state != ParserState.READY or len(res.args) != 2:
            continue

        total += res.args[0] * res.args[1]

    return total


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
        elif (
            op.type == MultOperation.type
            and op.state == ParserState.READY
            and is_enabled
        ):
            total += op.args[0] * op.args[1]

    return total, operations


if __name__ == "__main__":
    inp = parse_input()

    total_1 = solution_1(inp)

    print(f"Part one: {total_1}")

    total_2, operations_2 = solution_2(inp)

    print(f"Part two: {total_2}")
