from heapq import heapify,heappushpop,heappush
class Slope_Trick:
    def __init__(self):
        self.__L=[float("inf")]
        self.__R=[float("inf")]
        self.__y_min=0
        self.__add_L=self.__add_R=0

    def get_min(self):
        return self.__y_min

    def add(self,a):
        self.__y_min+=a

    def add_right(self,a):
        """ (x-a)^+:=max(0,x-a) を加算する.

        """
        l0=-self.__L[0]
        b=-heappushpop(self.__L,-a)
        heappush(self.__R,b)
        self.__y_min+=max(0,l0-a)

    def add_left(self,a):
        """ (x-a)^-:=max(0,-(x-a)) を加算する.

        """
        r0=self.__R[0]
        b=heappushpop(self.__R,a)
        heappush(self.__L,-b)
        self.__y_min+=max(0,a-r0)

    def add_both_side(self,a):
        """ abs(x-a) を加算する.

        """
        self.add_right(a)
        self.add_left(a)

    def argmin(self):
        """ f(x)=min f を満たす x の範囲を求める.
        """
        return (-self.__L[0]+self.__add_L,self.__R[0]+self.__add_R)

    def cumulative_left_min(self):
        """ min_{y<=x} f(y) に変更する.

        """

        self.__R=[float("inf")]

    def cumulative_right_min(self):
        """ min_{y>=x} f(x) を求める.

        """

        self.__L=[float("inf")]

    def slide(self,a):
        """ f(x-a) に変更する.

        """
        self.__add_L+=a
        self.__add_R+=a

    def sliding_window_minimum(self,a,b):
        """ min_{x-b<=y<=x-a} f(y) に変更する.
        """

        assert a<=b

        self.__add_L+=a
        self.__add_R+=b

    def copy(self):
        G=Slope_Trick()
        G.__L=self.__L.copy()
        G.__R=self.__R.copy()
        G.__add_L=self.__add_L
        G.__add_R=self.__add_R
        G.__y_min=self.__y_min
        return G