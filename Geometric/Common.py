class Common:
    error = 1e-8

    @classmethod
    def sign(cls, a):
        """ a の符号を求める.

        [return]
        a が負なら -1, 正なら +1, 0 は 0.
        """
        if a < -Common.error:
            return -1
        elif a > Common.error:
            return 1
        else:
            return 0

    @classmethod
    def compare(cls, x, y):
        """ x,y の大小を求める.

        [return]
        x > y ならば +1, x < y ならば -1, x = y ならば 0
        """
        return Common.sign(y-x)
