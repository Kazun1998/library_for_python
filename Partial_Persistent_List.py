class Partial_Persistent_List:
    def __init__(self, A, manual_mode=False):
        """ A を半永続リスト化する.

        manual_mode: False ならば代入すると自動的に時刻が進み, True ならば時刻は self.forward_time() で進めなければならない.
        """

        from bisect import bisect_left

        self.__N=N=len(A)
        self.mode=manual_mode

        self.__bis=bisect_left
        self.__set_time=[[-1] for _ in range(N)]
        self.__set_value=[[a] for a in A]
        self.__time=0

    def get_time(self):
        return self.__time

    def get_value(self, index, time=-1):
        if time>=0:
            j=self.__bis(self.__set_time[index], time)-1
        else:
            j=len(self.__set_time[index])-1
        return self.__set_value[index][j]

    def set_value(self, index, value):
        T=self.__set_time[index]
        V=self.__set_value[index]

        if T[-1]==self.__time:
            V[-1]=value
        else:
            T.append(self.__time)
            V.append(value)

        if not self.mode:
            self.__time+=1

    def forward_time(self):
        self.__time+=1

    def __len__(self):
        return self.__N

    def __str__(self):
        return str([self[i] for i in range(self.__N)])

    def __repr__(self):
        return repr([self[i] for i in range(self.__N)])

    def __iter__(self):
        for i in range(self.__N):
            yield self[i]

    def __setitem__(self, index, value):
        self.set_value(index, value)

    def __getitem__(self, index):
        return self.__set_value[index][-1]
