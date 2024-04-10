import sys
import re

string = sys.stdin.readline().rstrip()
# p = re.compile('[UCP]')
# result = p.findall(string)

success = "I love UCPC"
fail = "I hate UCPC"
# answer = success if "UCPC" == str.join("", result).strip() else fail

finds = ["U", "C", "P", "C", "finish"]
index = 0
for c in string:
    if finds[index] == c:
        index += 1
answer = success if finds[index] == "finish" else fail
print(answer)