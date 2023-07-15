import re
import sys


class MyPyError:
    """Represents a MyPy error."""

    def __init__(self, file: str, line: int = 0, col: int = 0, message: str = "error", warn: bool = False):
        self.file = file
        self.line = line
        self.col = col
        self.message = message
        self.warn = warn

    def __str__(self) -> str:
        kind = "warning" if self.warn else "error"
        return f"::{kind} file={self.file},line={self.line},col={self.col}::{self.message}"


class MyPyErrorParser:
    """Parses MyPy output and generates error objects."""

    MYPY_REGEX = (
        r"^(\w:)?(?P<file>[^:]+):(?P<line>\d+):((?P<col>\d+):)?"
        r"\s*(?P<type>[^:]+):\s*(?P<msg>.+)"
    )

    def __init__(self, output_file: str):
        self.output_file = output_file

    def parse_errors(self) -> list[MyPyError]:
        errors = []
        with open(self.output_file) as file:
            data = file.read()

        for line in data.split("\n"):
            match = re.match(self.MYPY_REGEX, line)
            if match:
                values = match.groupdict()
                error = MyPyError(
                    values["file"],
                    line=int(values["line"]),
                    col=int(values["col"]),
                    message=values["msg"],
                )
                errors.append(error)

        return errors


def main(file_path: str) -> None:
    """Reads the given file, parses MyPy errors, and prints them."""
    error_parser = MyPyErrorParser(file_path)
    errors = error_parser.parse_errors()

    for error in errors:
        print(error)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You must specify a file path!")
        sys.exit(1)
    file_path = sys.argv[1]
    main(file_path)
