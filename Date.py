class Date_Error(Exception):
    pass

class Date():
    Month_End=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    def __init__(self,Y,M,D):
        self.Y=Y
        self.M=M
        self.D=D

    def __str__(self):
        y=str(self.Y)
        m=str(self.M)
        d=str(self.D)
        return "{} / {} / {}".format(y,m.zfill(2),d.zfill(2))

    def __repr__(self):
        return self.__str__()

    def __eq__(self,other):
        return (self.Y==other.Y) and (self.M==other.M) and (self.D==other.D)

    def __neq__(self,other):
        return not(self==other)

    def __le__(self,other):
        if self.Y!=other.Y:
            return self.Y<other.Y
        elif self.M!=other.M:
            return self.M<other.M
        else:
            return self.D<=other.D

    def __lt__(self,other):
        return self<=other and self!=other

    def __ge__(self,other):
        return other<=self

    def __gt__(self,other):
        return other<self

    def is_leap_year(self):
        Y=self.Y
        if Y%4:
            return False
        elif Y%100:
            return True
        elif Y%400:
            return False
        else:
            return True

    def next_day(self, day=1):
        Y,M,D=self.Y,self.M,self.D

        x=400*365+97
        if Day>=x:
            t,Day=divmod(Day,x)
            Y+=400*t

        def leap(Y):
            if Y%4:
                return False
            elif Y%100:
                return True
            else:
                return (Y%400)==0

        T=leap(Y)
        for _ in range(Day):
            D+=1
            if (M!=2) and (self.Month_End[M]<D):
                D=1
                M=M%12+1
                Y+=1 if M==1 else 0

                if M==1:
                    T=leap(Y)

            elif (M==2) and (not T) and D>28:
                M,D=3,1
            elif (M==2) and T and D>29:
                M,D=3,1
        return Date(Y,M,D)

    def day_of_week(self):
        """曜日を求める.

        ※紀元後4年~紀元後1582年はユリウス歴での計算
        """
        Y,M,D=self.Y,self.M,self.D

        if M<=2:
            Y-=1
            M+=12

        C=Y//100
        if 1582<=Y:
            G=5*C+(C//4)
        else:
            G=6*C+5

        Y%=100

        a=D+(26*(M+1))//10+Y+(Y//4)+G
        h=a%7
        return ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"][h]

def Today():
    import datetime
    X=datetime.datetime.now()
    Y,M,D=X.year,X.month,X.day
    return Date(Y,M,D)
