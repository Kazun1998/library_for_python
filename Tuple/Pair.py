class Pair:
    __slot__=("first", "second")

    def __init__(self, first, second):
        self.first=first
        self.second=second

    def __str__(self):
        return "({}, {})".format(self.first, self.second)

    def __repr__(self):
        return "[Pair] : "+str(self)

    def __iter__(self):
        yield from [self.first, self.second]

    def __eq__(self, other):
        return (self.first==other.first) and (self.second==other.second)

    def __neq__(self, other):
        return not (self==other)

    def __le__(self, other):
        return (self.first<other.first) or (self.first==other.first and self.second<=other.second)

    def __lt__(self, other):
        return (self.first<other.first) or (self.first==other.first and self.second<other.second)

    def __ge__(self, other):
        return (self.first>other.first) or (self.first==other.first and self.second>=other.second)

    def __gt__(self, other):
        return (self.first>other.first) or (self.first==other.first and self.second>other.second)

    def __add__(self, other):
        return Pair(self.first+other.first, self.second+other.second)

    def __radd__(self, other):
        self.first+=other.first
        self.second+=other.second
        return self

    def __sub__(self, other):
        return Pair(self.first-other.first, self.second-other.second)

    def __rsub__(self, other):
        self.first-=other.first
        self.second-=other.second
        return self

    def __mul__(self, other):
        return Pair(self.first*other.first, self.second*other.second)

    def __rmul__(self, other):
        self.first*=other.first
        self.second*=other.second
        return self

    def __floordiv__(self, other):
        return Pair(self.first//other.first, self.second//other.second)

    def __rfloordiv__(self, other):
        self.first//=other.first
        self.second//=other.second
        return self

    def __truediv__(self, other):
        return Pair(self.first/other.first, self.second/other.second)

    def __rtruediv__(self, other):
        self.first/=other.first
        self.second/=other.second
        return self
