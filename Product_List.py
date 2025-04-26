from typing import TypeVar, Generic

A = TypeVar('A')
class Product_List_2D(Generic[A]):
    def __init__(self, H: int, W: int, default: A = None):
        """ H x W の直積リストを生成する.

        Args:
            H (int): 第 1 引数
            W (int): 第 2 引数
            default (A, optional): 各要素の初期状態. Defaults to None.
        """

        self._H = H
        self._W = W
        self._default = default
        self._list = [default] * (H * W)

    @property
    def H(self) -> int:
        """ 第 1 引数の個数

        Returns:
            int: 第 1 引数の個数
        """
        return self._H

    @property
    def W(self) -> int:
        """ 第 2 引数の個数

        Returns:
            int: 第 2 引数の個数
        """
        return self._W

    def __to_index(self, i: int, j: int) -> bool:
        if i < 0:
            i = ~i
        if j < 0:
            j = ~j

        if (0 <= i < self._H) and (0 <= j < self._W):
            return i, j
        else:
            raise IndexError

    def __len__(self) -> int:
        return self.H * self.W

    def get(self, i: int, j: int) -> A:
        """ 第 (i, j) 要素を得る.

        Args:
            i (int): 第 1 引数
            j (int): 第 2 引数

        Returns:
            A: 第 (i, j) 要素
        """

        i, j = self.__to_index(i, j)
        return self._list[i * self.W + j]

    def get_all(self):
        return [self._list[i * self._W: (i + 1) * self._W] for i in range(self._H)]

    def set(self, i: int, j: int, value: A) -> A:
        """ 第 (i, j) 要素を value にする.

        Args:
            i (int): 第 1 引数
            j (int): 第 2 引数
            value (A): 更新後の要素

        Returns:
            A: value
        """

        i, j = self.__to_index(i, j)
        self._list[i * self.W + j] = value
        return value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(H={self.H}, W={self.W}, default={self._default})"

class Product_List_3D:
    def __init__(self, default, H, W, D):
        """ H x W x D の直積リストを生成する. """

        self.H=H
        self.W=W
        self.D=D
        self.list=[default]*(H*W*D)

    def __len__(self):
        return self.H*self.W*self.D

    def get(self, i, j, k):
        if i<0:
            i+=self.H

        if j<0:
            j+=self.W

        if k<0:
            k+=self.D

        return self.list[(i*self.W+j)*self.D+k]

    def get_all(self):
        return [[[self.get(i,j,k) for k in range(self.D)] for j in range(self.W)] for i in range(self.H)]

    def projection_H(self, i):
        if i<0:
            i+=self.H

        return [self.projection_HW(i,j) for j in range(self.W)]

    def projection_HW(self, i, j):
        if i<0:
            i+=self.H

        if j<0:
            j+=self.W

        start=(i*self.W+j)*self.D
        return self.list[start: start+self.D]

    def set(self, i, j, k, value):
        if i<0:
            i+=self.H

        if j<0:
            j+=self.W

        if k<0:
            k+=self.D

        self.list[(i*self.W+j)*self.D+k]=value

    def set_once(self, i, j, A):
        if i<0:
            i+=self.H

        if j<0:
            j+=self.W

        index=(i*self.W+j)*self.D
        for j in range(self.D):
            self.list[index]=A[j]
            index+=1

    def __getitem__(self, index):
        return self.get(index[0], index[1], index[2])

    def __setitem__(self, index, value):
        self.set(index[0], index[1], index[2], value)

    def __repr__(self):
        return "[Product List 3D] : Height: {}, Width: {}, Depth: {}".format(self.H, self.W, self.D)

class Product_List_4D:
    def __init__(self, default, H, W, D, T):
        """ H x W x D x T の直積リストを生成する. """

        self.H=H
        self.W=W
        self.D=D
        self.T=T
        self.list=[default]*(H*W*D*T)

    def __len__(self):
        return self.H*self.W*self.D*self.T

    def get(self, i, j, k, l):
        if i<0:
            i+=self.H

        if j<0:
            j+=self.W

        if k<0:
            k+=self.D

        if l<0:
            l+=self.T

        return self.list[((i*self.W+j)*self.D+k)*self.T+l]

    def get_all(self):
        return [[[[self.get(i,j,k,l) for l in range(self.T)] for k in range(self.D)] for j in range(self.W)] for i in range(self.H)]

    def set(self, i, j, k, l, value):
        if i<0:
            i+=self.H

        if j<0:
            j+=self.W

        if k<0:
            k+=self.D

        if l<0:
            l+=self.T

        self.list[((i*self.W+j)*self.D+k)*self.T+l]=value

    def set_once(self, i, j, k, A):
        if i<0:
            i+=self.H

        if j<0:
            j+=self.W

        if k<0:
            k+=self.D

        index=((i*self.W+j)*self.D+k)*self.T
        for j in range(self.T):
            self.list[index]=A[j]
            index+=1

    def __getitem__(self, index):
        return self.get(index[0], index[1], index[2], index[3])

    def __setitem__(self, index, value):
        self.set(index[0], index[1], index[2], index[3], value)

    def __repr__(self):
        return "[Product List 4D] : Height: {}, Width: {}, Depth: {}, Time: {}".format(self.H, self.W, self.D, self.T)
