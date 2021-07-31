from typing import NamedTuple, Tuple


class Index(NamedTuple):
    row: int
    col: int


def validate_index(
    index: Tuple[int, int], rows: int, cols: int
) -> Tuple[int, int]:
    if not isinstance(index, tuple) or len(index) != 2:
        raise IndexError("Invalid number of indices")
    row, col = index
    if not 0 <= row < rows:
        raise IndexError("Row index out of range")
    if not 0 <= col < cols:
        raise IndexError("Column index out of range")
    return Index(row, col)
