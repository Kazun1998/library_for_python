class Slide_Window():
    """ 積をスライドさせながらもとめる.
    """

    __slots__=("calc", "__front", "__back", "__left", "__right", "__cnt")

    def __init__(self,calc,X=[]):
        """スライドプロダクトクラスを生成する.

        calc: 2項演算 (半群)
        ※calcについて, 右から新しい項を加えること.
        """
        from collections import deque
        self.calc=calc
        self.__front=deque()
        self.__left=deque()
        self.__back=deque()
        self.__right=deque()
        self.__cnt=0

        for x in X:
            if self.__right:
                self.__right.append(self.calc(self.__right[-1], x))
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

    __repr__=__str__

    def __len__(self):
        return self.__cnt

    def __bool__(self):
        return self.__cnt>0

    def push(self, x, k=1):
        """ x を k 回 push する.

        x: value
        k: 回数
        """
        self.__cnt+=1

        self.__back.append(x)

        if self.__right:
            self.__right.append(self.calc(self.__right[-1],x))
        else:
            self.__right.append(x)

    def pop(self, k=1):
        """ k 回 push する.

        k: 回数
        """

        for _ in range(min(k,self.__cnt)):
            if not self.__front:
                self.__right.clear()
                while self.__back:
                    x=self.__back.pop()

                    if self.__front:
                        self.__left.appendleft(self.calc(x,self.__left[0]))
                    else:
                        self.__left.appendleft(x)
                    self.__front.appendleft(x)

            self.__front.popleft()
            self.__left.popleft()

        self.__cnt-=min(k,self.__cnt)

    def product(self, default=None):
        """ 積を求める.

        default: 空のときの返り値を設定する.
        """

        if self.__front:
            if self.__back:
                return self.calc(self.__left[0],self.__right[-1])
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
