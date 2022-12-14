class Product_List_2D:
    def __init__(self, default, H, W):
        """ H x W の直積リストを生成する. """

        self.H=H
        self.W=W
        self.list=[default]*(H*W)

    def __len__(self):
        return self.H*self.W

    def get(self, i, j):
        if i<0:
            i+=self.H

        if j<0:
            j+=self.W

        return self.list[i*self.W+j]

    def get_all(self):
        return [self.list[i*self.W: (i+1)*self.W] for i in range(self.H)]

    def projection_H(self, i):
        if i<0:
            i+=self.H

        return self.list[i*self.W: (i+1)*self.W]

    def set(self, i, j, value):
        if i<0:
            i+=self.H

        if j<0:
            j+=self.W

        self.list[i*self.W+j]=value

    def set_once(self, i, A):
        if i<0:
            i+=self.H

        index=i*self.W
        for j in range(self.W):
            self.list[index]=A[j]
            index+=1

    def __getitem__(self, index):
        return self.get(index[0], index[1])

    def __setitem__(self, index, value):
        self.set(index[0], index[1], value)

    def __repr__(self):
        return "[Product List 2D] : Height: {}, Width: {}".format(self.H, self.W)

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
