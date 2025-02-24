from typing import TypeVar, Generic, Callable

M = TypeVar('M')
class Monoided_Functional_Graph(Generic[M]):
    def __init__(self, N: int, K: int, op: Callable[[M, M], M], unit: M):
        """ 有向辺にモノイドの重みを乗せた Functional Graph を生成する.

        Args:
            N (int): 頂点数 (0,1,2,...,N-1 を生成する)
            K (int): 計算に必要な最大の指数
            op (Callable[[M, M], M]): モノイドの演算 op(new, old)
            unit (M): 単位元
        """

        self.N=N
        self.K=K
        self.op=op
        self.unit=unit

        self.out=[list(range(N))]
        self.value=[[unit]*N]

    def set_arc(self, source: int, target: int, x: M) -> None:
        """ 重み x で有向辺 source -> target を設定する

        Args:
            source (int): 始点
            target (int): 終点
            x (M): 重み
        """

        self.out[0][source]=target
        self.value[0][source]=x

    def build(self) -> None:
        """ Functional Graph を確定させる.
        """

        # 1 段階目は元の情報であるから省略
        K = self.K >> 1
        N = self.N
        op = self.op

        while K:
            prev_out = self.out[-1]
            current_out = [0] * N
            prev_value = self.value[-1]
            current_value = [None] * N

            for i in range(N):
                p = prev_out[i]; x = prev_value[i]
                q = prev_out[p]; y = prev_value[p]

                current_out[i] = q
                current_value[i] = op(y, x)

            self.out.append(current_out)
            self.value.append(current_value)
            K >>= 1

    def calculate(self, v: int, k: int) -> M:
        """ 頂点 v から k 回移動したときの累積重みを求める.

        Args:
            v (int): 始点
            k (int): 移動回数

        Returns:
            M: 累積重み
        """
        x = self.unit
        op = self.op
        out = self.out
        value = self.value
        for out, value in zip(out, value):
            if k & 1:
                x = op(value[v], x)
                v = out[v]
            k >>= 1

        return x
