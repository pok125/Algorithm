import itertools

n = int(input())
num_list = list(map(int, input().split(' ')))
operator_count = list(map(int, input().split(' ')))
operator = ['+', '-', '*', '/']
s = ''

for i in range(len(operator)):
    s += operator[i] * operator_count[i]

result = 0
answer = []
l = set(itertools.permutations(s, n - 1))

for oper in l: 
    result = num_list[0]
    for i in range(1, n):
        match (oper[i - 1]):
            case '+':
                result += num_list[i]
            case '-':
                result -= num_list[i]
            case '*':
                result *= num_list[i]
            case '/':
                if result < 0:
                    result *= -1 
                    result //= num_list[i]
                    result *= -1
                else:
                    result //= num_list[i]
     
    answer.append(result)

print(max(answer))
print(min(answer))