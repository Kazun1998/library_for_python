from Point import *
class Line():
    __slots__=["P","Q","id"]

    def __init__(self,P,Q):
        "2点 P, Qを通る直線を生成する."""
        assert P!=Q
