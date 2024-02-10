class Segment_Division:
    def __init__(self, N: int):
        self.N = N
        self.depth = max(1, (N - 1).bit_length())
        self.size = 1 << self.depth

        self.range = [None] * (self.size) + [(i, i) for i in range(self.N)] + [None] * (self.size - self.N)

        for i in range(self.size - 1, 0, -1):
            if (self.range[2 * i] is not None) and (self.range[2 * i + 1] is not None):
                self.range[i] = (self.range[2 * i][0], self.range[2 * i + 1][1])

    def interval(self, left: int, right: int, left_closed = True, right_closed = True):
        assert (0 <= left < self.size) and (0 <= right < self.size)

        l = left + self.size + (not left_closed)
        r = right + self.size + (right_closed)

        left_seg = []
        right_seg = []
        while l < r:
            if l & 1:
                yield self.range[l]
                l += 1

            if r & 1:
                r -= 1
                yield self.range[r]

            l >>= 1
            r >>= 1

        return left_seg + right_seg[::-1]

    def all_segments(self):
        return [seg for seg in self.range[1:] if seg is not None]
