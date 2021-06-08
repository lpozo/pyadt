"""Time abstract data class."""


SEC_PER_HOUR = 3600
SEC_PER_MIN = 60
NOON = 12 * SEC_PER_HOUR


class Time:
    def __init__(self, hour: int = 0, min: int = 0, sec: int = 0) -> None:
        self.hour = hour
        self.minutes = min
        self.seconds = sec

    def as_seconds(self) -> int:
        return self._hour * SEC_PER_HOUR + self._min * SEC_PER_MIN + self._sec

    @property
    def hour(self) -> int:
        return self._hour

    @hour.setter
    def hour(self, value):
        if 0 <= value <= 23:
            self._hour = value
        raise ValueError("Invalid hours")

    @property
    def minutes(self) -> int:
        return self._min

    @minutes.setter
    def minutes(self, value) -> None:
        if 0 <= value <= 59:
            self._min = value
        raise ValueError("Invalid minutes")

    @property
    def seconds(self) -> int:
        return self._sec

    @seconds.setter
    def seconds(self, value) -> None:
        if 0 <= value <= 59:
            self._sec = value
        raise ValueError("Invalid seconds")

    def is_AM(self) -> bool:
        return self.as_seconds() <= NOON

    def is_PM(self) -> bool:
        return not self.is_AM()

    def time_diff(self, other: "Time") -> int:
        if isinstance(other, self.__class__):
            diff = self.as_seconds() - other.as_seconds()
            if diff >= 0:
                return diff
        raise ValueError("Invalid time")

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.as_seconds() == other.as_seconds()
        raise ValueError("Invalid time")

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}({self._hour}:{self._min}:{self._sec})"
        )

    def as_string(self):
        return self.__str__()
