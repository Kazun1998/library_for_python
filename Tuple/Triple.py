class Triple:
    __slot__=("first", "second", "third")

    def __init__(self, first, second, third):
        self.first=first
        self.second=second
        self.third=third

    def __str__(self):
        return "({}, {}, {})".format(self.first, self.second, self.third)

    def __repr__(self):
        return "[Triple] : "+str(self)

    def __iter__(self):
        yield from [self.first, self.second, self.third]

    def __eq__(self, other):
        return (self.first==other.first) and (self.second==other.second) and (self.thrid==other.third)

    def __neq__(self, other):
        return not (self==other)

    def __le__(self, other):
        f=(self.first<other.first)
        g=(self.first==other.first and self.second<other.second)
        h=(self.first==other.first and self.second==self.second and self.third<=other.third)
        return  f or g or h

    def __lt__(self, other):
        f=(self.first<other.first)
        g=(self.first==other.first and self.second<other.second)
        h=(self.first==other.first and self.second==self.second and self.third<other.third)
        return  f or g or h

    def __ge__(self, other):
        f=(self.first>other.first)
        g=(self.first==other.first and self.second>other.second)
        h=(self.first==other.first and self.second==self.second and self.third>=other.third)
        return  f or g or h

    def __gt__(self, other):
        f=(self.first>other.first)
        g=(self.first==other.first and self.second>other.second)
        h=(self.first==other.first and self.second==self.second and self.third>other.third)
        return  f or g or h

    def __add__(self, other):
        return Triple(self.first+other.first, self.second+other.second, self.third+other.third)

    def __radd__(self, other):
        self.first+=other.first
        self.second+=other.second
        self.third+=other.third
        return self

    def __sub__(self, other):
        return Triple(self.first-other.first, self.second-other.second, self.third-other.third)

    def __rsub__(self, other):
        self.first-=other.first
        self.second-=other.second
        self.third-=other.third
        return self

    def __mul__(self, other):
        return Triple(self.first*other.first, self.second*other.second, self.third*other.third)

    def __rmul__(self, other):
        self.first*=other.first
        self.second*=other.second
        self.third*=other.third
        return self

    def __floordiv__(self, other):
        return Triple(self.first//other.first, self.second//other.second, self.third//other.third)

    def __rfloordiv__(self, other):
        self.first//=other.first
        self.second//=other.second
        self.third//=other.third
        return self

    def __truediv__(self, other):
        return Triple(self.first/other.first, self.second/other.second, self.third/other.third)

    def __rtruediv__(self, other):
        self.first/=other.first
        self.second/=other.second
        self.third/=other.third
        return self
