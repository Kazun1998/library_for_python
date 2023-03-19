class Sliding_Window_Aggregation():
    """ 積をスライドさせながらもとめる.
    """

    __slots__=("op", "__front", "__back", "__left", "__right", "__cnt")

    def __init__(self, op, X=[]):
        """スライドプロダクトクラスを生成する.

        op: 2項演算 (半群)
        ※opについて, 右から新しい項を加えること.
        """
        from collections import deque
        self.op=op
        self.__front=deque()
        self.__left=deque()
        self.__back=deque()
        self.__right=deque()
        self.__cnt=0

        for x in X:
            if self.__right:
                self.__right.append(self.op(self.__right[-1], x))
            else:
                self.__right.append(x)

            self.__cnt+=1
            self.__back.append(x)

    def __str__(self):
        if self.__front:
            if self.__back:
                return str(self.__front)[6:-2]+", "+str(self.__back)[7:-1]
            else:
                return str(self.__front)[6:-1]
        else:
            return str(self.__back)[6:-1]

    def __repr__(self):
        return "Slide Product: "+str(self)+": product: {}".format(self.product())

    def __len__(self):
        return self.__cnt

    def __bool__(self):
        return self.__cnt>0

    def push(self, x):
        """ x を push する.

        x: value
        """

        self.__cnt+=1

        self.__back.append(x)

        if self.__right:
            self.__right.append(self.op(self.__right[-1],x))
        else:
            self.__right.append(x)

    def pop(self):
        """ push する.

        """

        if not self.__front:
            self.__right.clear()
            while self.__back:
                x=self.__back.pop()

                if self.__front:
                    self.__left.appendleft(self.op(x,self.__left[0]))
                else:
                    self.__left.appendleft(x)
                self.__front.appendleft(x)

        self.__front.popleft()
        self.__left.popleft()

    def product(self, default=None):
        """ 積を求める.

        default: 空のときの返り値を設定する.
        """

        if self.__front:
            if self.__back:
                return self.op(self.__left[0],self.__right[-1])
            else:
                return self.__left[0]
        else:
            if self.__back:
                return self.__right[-1]
            else:
                return default

    def clear(self):
        """ 初期化する. """

        self.__front.clear()
        self.__back.clear()
        self.__left.clear()
        self.__right.clear()
        self.__cnt=0
