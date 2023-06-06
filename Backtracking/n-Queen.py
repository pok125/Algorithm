class NQueen:
    def __init__(self, N):
        self.v_col = set()
        self.vplus_diagonal = set()
        self.vminus_diagonal = set()
        self.ans = 0
        self.N = N
        return
    
    def solve(self, row):
        # 끝의 행까지 도달
        if row == self.N:
            self.ans += 1
            return
        # 놓을 수 있는 위치 찾기
        for i in range(self.N):
            # 놓을 수 있다면 다음 행으로
            if self.check((row, i)):
                self.v_col.add(i)
                self.vplus_diagonal.add(row + i)
                self.vminus_diagonal.add(row - i)
                
                self.solve(row + 1)
                
                self.v_col.remove(i)
                self.vplus_diagonal.remove(row + i)
                self.vminus_diagonal.remove(row - i)

    def check(self, pos):
        # 열 체크
        if pos[1] in self.v_col:
            return False
        # 대각 체크
        if (pos[0] + pos[1]) in self.vplus_diagonal:
            return False
        if (pos[0] - pos[1]) in self.vminus_diagonal:
            return False
        return True
    
    def answer(self):
        self.solve(0)
        return self.ans

print(NQueen(8).answer())
