"""Matrix abstract data type."""

from typing import Any, List, Sequence, Tuple


class Matrix:
    """Build a matrix as an m × n rectangular grid."""

    def __init__(self, rows: int, cols: int, default: int = 0) -> None:
        self._rows = rows
        self._cols = cols
        self._data = [[default] * cols for _ in range(rows)]

    @classmethod
    def from_sequence(
        cls,
        sequence: Sequence[Sequence[Any]],
    ) -> "Matrix":
        """Return a new matrix built from a sequence of sequences."""
        if len(set(len(row) for row in sequence)) > 1:
            raise ValueError("invalid matrix size")
        matrix = cls(rows=len(sequence), cols=len(sequence[0]))
        for row, values in enumerate(sequence):
            for col, value in enumerate(values):
                matrix[row, col] = value
        return matrix

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

    def scale_by(self, scalar: int) -> None:
        for row in range(self._rows):
            for col in range(self._cols):
                self[row, col] *= scalar

    @property
    def size(self) -> Tuple[int, int]:
        return self._rows, self._cols

    def transpose(self) -> "Matrix":
        transposed = type(self)(self._cols, self._rows)
        transposed._data = [list(row) for row in zip(*self._data)]
        return transposed

    def add(self, other) -> "Matrix":
        if not (other.__class__ is self.__class__):
            raise TypeError("can only add matrix to matrix")
        if other.size == self.size:
            matrix = type(self)(self._rows, self._cols)
            for row in range(self._rows):
                for col in range(self._cols):
                    matrix[row, col] = self[row, col] + other[row, col]
            return matrix
        raise ValueError("invalid matrix size")

    def subtract(self, other) -> "Matrix":
        if not (other.__class__ is self.__class__):
            raise TypeError("can only subtract matrix from matrix")
        if other.size == self.size:
            matrix = type(self)(self._rows, self._cols)
            for row in range(self._rows):
                for col in range(self._cols):
                    matrix[row, col] = self[row, col] - other[row, col]
            return matrix
        raise ValueError("invalid matrix size")

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(\n\t"
            + "\n\t".join(str(row) for row in self._data)
            + "\n)"
        )

    def mutiply(self, other) -> "Matrix":
        if not (other.__class__ is self.__class__):
            raise TypeError("can only multiply matrix by matrix")
        if self._cols != other._rows:
            raise ValueError("invalid matrix size")

        matrix = type(self)(self.rows, other.cols)
        for i in range(self.rows):
            # iterate through columns of Y
            for j in range(other.cols):
                # iterate through rows of Y
                for k in range(other.rows):
                    matrix[i, j] += self[i, k] * other[k, j]
        return matrix

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(rows={self._rows}, cols={self._cols})"
        )

    def __getitem__(self, index: Tuple[int, int]) -> Any:
        row, col = self._validate_indices(index)
        return self._data[row][col]

    def __setitem__(self, index: Tuple[int, int], value: Any) -> None:
        row, col = self._validate_indices(index)
        self._data[row][col] = value

    def _validate_indices(self, index: Tuple[int, int]) -> Tuple[int, int]:
        if not isinstance(index, tuple) or len(index) != 2:
            raise IndexError("Invalid number of indices")
        row, col = index
        if not 0 <= row < self._rows:
            raise IndexError("Row index out of range")
        if not 0 <= col < self._cols:
            raise IndexError("Column index out of range")
        return index


m = Matrix.from_sequence([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m)
