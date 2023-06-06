input_string = input()
l = input_string.split('-')
for i in range(len(l)):
     l[i] = sum(map(int, l[i].split('+')))

result = l[0]
for i in range(1, len(l)):
     result -= l[i]
     
print(result)