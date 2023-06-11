# nQueen 문제

class NQueen:
    def __init__(self, n):
        self.check_col = set()
        self.check_plus_diagonal = set()
        self.check_minus_diagonal = set()
        self.size = n
        self.result = 0
    
    def check_position(self, pos):
        # 열 체크
        if pos[0] in self.check_col:
            return False

        # plus대각 체크
        if (pos[0] + pos[1]) in self.check_plus_diagonal:
            return False

        # minus대각 체크
        if (pos[0] - pos[1]) in self.check_minus_diagonal:
            return False
    
        return True
    
    def solving(self, row):
        if row >= self.size:
            self.result += 1
            return
        
        for col in range(self.size):
            if self.check_position((col, row)):
                self.check_col.add(col)
                self.check_plus_diagonal.add(col + row)
                self.check_minus_diagonal.add(col - row)
                self.solving(row + 1)
                self.check_col.remove(col)
                self.check_plus_diagonal.remove(col + row)
                self.check_minus_diagonal.remove(col - row)
    
    def answer(self):
        self.solving(0)
        return self.result

n = int(input())
print(NQueen(n).answer())


