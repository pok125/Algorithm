'''
다이나믹 프로그래밍 알고리즘 조건
1. 문제를 여러 서브 문제로 나눌 수 있는가
2. 서브 문제들의 해를 통해 큰 문제의 해를 도출할 수 있는가
3. 동일한 서브 문제들이 존재하는가
'''

# 일반적 풀이
def custom_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    result = custom_fibo(n - 1) + custom_fibo(n - 2)
    return result

# dp 풀이
# 문제점 recursion maximum call stack 발생
def dp_fibo(n):
    f = [0, 1]

    if n < len(f):
        return f[n]
    else:
        result = dp_fibo(n - 1) + dp_fibo(n - 2)
        f.append(result)
        return result
    
# bottom-up 풀이
def dp_fibo2(n):
    f = [0, 1]

    for i in range(2, n + 1):
        num = f[i - 1] + f[i - 2]
        f.append(num)
    return f[n]