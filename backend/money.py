class money:
    cents: int = 0

    def __init__(self, value: float, cents: bool = False):
        if cents:
            self.cents = int(value)
        else:
            self.cents = round(value * 100)

    def __repr__(self) -> str:
        return f'<{type(self).__name__}: {self}>'

    def __str__(self) -> str:
        return str(self.cents / 100)

    def __add__(self, other) -> 'money':
        if type(other) in [float, int]:
            return self + type(self)(other)

        elif type(other) is type(self):
            return_obj = self.clone()
            return_obj.cents += other.cents
            return return_obj
        else:
            raise TypeError()

    def __radd__(self, other) -> 'money':
        return self + other

    def __neg__(self) -> 'money':
        return_obj = self.clone()
        return_obj.cents = -return_obj.cents
        return return_obj

    def __rneg__(self, other) -> 'money':
        return self - other

    def __sub__(self, other) -> 'money':
        return self + (-other)

    def clone(self) -> 'money':
        return type(self).from_cents(self.cents)

    def to_float(self) -> float:
        return self.cents / 100

    def __float__(self) -> float:
        return self.to_float()

    def __eq__(self, other) -> bool:
        if type(other) in [float, int]:
            return float(self) == other
        elif type(other) is type(self):
            return self.cents == other.cents
        else:
            raise TypeError()

    def __ne__(self, other) -> bool:
        return not (self == other)

    def __lt__(self, other) -> bool:
        if type(other) in [float, int]:
            return float(self) < other
        elif type(other) is type(self):
            return self.cents < other.cents
        else:
            raise TypeError()

    def __le__(self, other) -> bool:
        return self < other or self == other

    def __ge__(self, other) -> bool:
        return not self < other

    def __gt__(self, other) -> bool:
        return (not self < other) and self != other

    def __hash__(self):
        return hash(self.cents)

    @classmethod
    def from_cents(cls, value: int) -> 'money':
        c = cls(value, cents=True)
        return c
