m = int(input())
score = [list(map(int, input().split(" "))) for _ in range(m)]
answer = []
def solving(n, team_one, team_two):
    if n == m:
        one_len = len(team_one)
        two_len = len(team_two)
    
        if one_len == two_len:
            team_one_score = 0
            team_two_score = 0
           
            for i in range(one_len):
                for j in range(one_len):
                    team_one_score += score[team_one[i]][team_one[j]]
                    team_two_score += score[team_two[i]][team_two[j]]
                
            answer.append(abs(team_one_score - team_two_score))
        
        return
    
    solving(n + 1, team_one + [n], team_two)
    solving(n + 1, team_one, team_two + [n])

solving(0, [], [])
print(min(answer))