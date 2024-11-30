class Cartesian_Tree:
    def __init__(self, sequence: list):
        self.sequence = sequence
        self.N = len(sequence)
        self.left = [-1] * self.N
        self.right = [-1] * self.N
        self.parent = [-1] * self.N
        self.root = -1

        self._build()

    def _build(self):
        A = self.sequence
        stack = []

        for i in range(self.N):
            if i == 0:
                stack.append(0)
                self.root = 0
                continue

            last_pop = None
            while stack and A[stack[-1]] >= A[i]:
                last_pop = stack.pop()

            # 左の子に関する設定
            if last_pop is not None:
                self.left[i] = last_pop
                self.parent[last_pop] = i

            # 右の子に関する設定
            if stack:
                self.right[stack[-1]] = i
                self.parent[i] = stack[-1]
            else:
                self.root = i

            stack.append(i)
