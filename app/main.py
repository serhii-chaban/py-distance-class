from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, new: Distance | float | int) -> Distance:
        if isinstance(new, Distance):
            return Distance(self.km + new.km)
        return Distance(self.km + new)

    def __iadd__(self, new: Distance | float | int) -> Distance:
        if isinstance(new, Distance):
            self.km += new.km
            return self
        self.km += new
        return self

    def __mul__(self, new: float | int) -> Distance:
        return Distance(self.km * new)

    def __truediv__(self, new: int | float) -> Distance | None:
        if new:
            return Distance(round(self.km / new, 2))
        return

    def __lt__(self, new: Distance | float | int) -> bool:
        if isinstance(new, Distance) and self.km < new.km:
            return True
        elif self.km < new:
            return True
        return False

    def __gt__(self, new: Distance | float | int) -> bool:
        if isinstance(new, Distance) and self.km > new.km:
            return True
        elif self.km > new:
            return True
        return False

    def __eq__(self, new: Distance | float | int) -> bool:
        if isinstance(new, Distance) and self.km == new.km:
            return True
        elif self.km == new:
            return True
        return False

    def __le__(self, new: Distance | float | int) -> bool:
        if isinstance(new, Distance) and self.km <= new.km:
            return True
        elif self.km <= new:
            return True
        return False

    def __ge__(self, new: Distance | float | int) -> bool:
        if isinstance(new, Distance) and self.km >= new.km:
            return True
        elif self.km >= new:
            return True
        return False
