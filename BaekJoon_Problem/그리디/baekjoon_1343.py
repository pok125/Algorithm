import re

input_string = input()
while re.findall('(XXXX)', input_string):
    input_string = re.sub('(XXXX)', 'AAAA', input_string)

while re.findall('(XX)', input_string):
    input_string = re.sub('(XX)', 'BB', input_string)

if 'X' in input_string:
    print(-1)
else:
    print(input_string)