class Sliding_Window_Aggregation_Both_Sides:
    def __init__(self, calc):
        """ 両側スライドプロダクトクラスを生成する.

        calc: 2項演算 (半群)
        ※calcについて, front は左から, back は右から行う.
        """

        self.calc=calc
        self.left_value=[]
        self.left_prod=[]
        self.right_value=[]
        self.right_prod=[]

    def __str__(self):
        if self.left_value:
            if self.right_value:
                return str(self.left_value[::-1])[:-1]+", "+str(self.right_value)[1:]
            else:
                return str(self.left_value[::-1])
        else:
            return str(self.right_value)

    def __repr__(self):
        return "Slide Product Both Side: "+str(self)+": product: {}".format(self.product())

    def __len__(self):
        return len(self.left_value)+len(self.right_value)

    def __bool__(self):
        return bool(len(self))

    def push_front(self, x):
        self.left_value.append(x)
        if self.left_prod:
            self.left_prod.append(self.calc(x, self.left_prod[-1]))
        else:
            self.left_prod.append(x)

    def push_back(self, x):
        self.right_value.append(x)
        if self.right_prod:
            self.right_prod.append(self.calc(self.right_prod[-1], x))
        else:
            self.right_prod.append(x)

    def pop_front(self):
        if not self.left_prod:
            rm=len(self.right_prod)//2
            lm=len(self.right_prod)-rm

            self.right_prod.clear()
            T=[self.right_value.pop() for _ in range(rm)]

            for _ in range(lm):
                y=self.right_value.pop()
                self.left_value.append(y)
                if self.left_prod:
                    self.left_prod.append(self.calc(y, self.left_prod[-1]))
                else:
                    self.left_prod.append(y)

            for _ in range(rm):
                y=T.pop()
                self.right_value.append(y)
                if self.right_prod:
                    self.right_prod.append(self.calc(self.right_prod[-1], y))
                else:
                    self.right_prod.append(y)

        self.left_value.pop()
        self.left_prod.pop()

    def pop_back(self):
        if not self.right_prod:
            lm=len(self.left_prod)//2
            rm=len(self.left_prod)-lm

            self.left_prod.clear()
            T=[self.left_value.pop() for _ in range(lm)]

            for _ in range(rm):
                y=self.left_value.pop()
                self.right_value.append(y)
                if self.right_prod:
                    self.right_prod.append(self.calc(self.right_prod[-1], y))
                else:
                    self.right_prod.append(y)

            for _ in range(lm):
                y=T.pop()
                self.left_value.append(y)
                if self.left_prod:
                    self.left_prod.append(self.calc(y, self.left_prod[-1]))
                else:
                    self.left_prod.append(y)

        self.right_value.pop()
        self.right_prod.pop()

    def product(self, default=None):
        if self.right_prod:
            if self.left_prod:
                return self.calc(self.left_prod[-1], self.right_prod[-1])
            else:
                return self.right_prod[-1]
        else:
            if self.left_prod:
                return self.left_prod[-1]
            else:
                return default

    def clear(self):
        """ 初期化する. """

        self.left_value.clear()
        self.left_prod.clear()
        self.right_value.clear()
        self.right_prod.clear()

