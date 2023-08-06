S1 = input()
S2 = input()
S1_len = len(S1)
S2_len = len(S2)

LCS = [[0] * S1_len for _ in range(S2_len)]
