class Mo:
    def __init__(self, N):
        """ 範囲が 0 以上 N "未満" の Mo's Algorithm の準備をする.

        """
        self.N=N
        self.Q=0
        self.left=[]
        self.right=[]

    def add_query(self, l, r):
        """ 閉区間 [l,r] に対するクエリを追加する.
        """

        self.left.append(l)
        self.right.append(r+1)
        self.Q+=1

    def calculate(self, add, delete, rem):
        """ クエリを処理する.

        """

        block_size=self.N//(min(self.N, int(self.Q**0.5+0.5)))
        t=(self.N+block_size-1)//block_size
        B=[[] for _ in range(t)]

        left=self.left; right=self.right

        for q in range(self.Q):
            B[left[q]//block_size].append(q)

        for i in range(t):
            B[i].sort(key=lambda q: right[q], reverse=i%2)

        x=y=0
        for b in B:
            for q in b:
                l=left[q]; r=right[q]
                for i in range(x, l):
                    delete(i)

                for i in range(x-1, l-1, -1):
                    add(i)

                for j in range(y, r):
                    add(j)

                for j in range(y-1, r-1, -1):
                    delete(j)

                x=l; y=r
                rem(q)
        return

    def calculate_noncommutative(self, add_left, add_right, delete_left, delete_right, rem):
        block_size=self.N//(min(self.N, int(self.Q**0.5+0.5)))
        t=(self.N+block_size-1)//block_size
        B=[[] for _ in range(t)]

        left=self.left; right=self.right

        for q in range(self.Q):
            B[left[q]//block_size].append(q)

        for i in range(t):
            B[i].sort(key=lambda q: right[q], reverse=i%2)

        x=y=0
        for b in B:
            for q in b:
                l=left[q]; r=right[q]

                for i in range(x, l):
                    delete_left(i)

                for i in range(x-1, l-1, -1):
                    add_left(i)

                for j in range(y, r):
                    add_right(j)

                for j in range(y-1, r-1, -1):
                    delete_right(j)

                x=l; y=r
                rem(q)
        return
    
