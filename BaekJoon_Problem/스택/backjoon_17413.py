# 단어 뒤집기 2

# <ab cd>fe hg<ij kl>
import sys
string = sys.stdin.readline()
flag = False
stack = []
answer = []
temp_list = []
word = ""
string = string.rstrip()
string += " "
for char in string:
    if flag == False and char == " ":
        temp = str.join("", temp_list)
        temp_list.clear()
        while stack:
            temp += stack.pop()
        answer.append(temp)
    elif char == "<":
        word += char
        flag = True
    elif char == ">":
        word += char
        flag = False
        if stack:
            temp = ""
            while stack:
                temp += stack.pop()
            word = temp + word
        temp_list.append(word)    
        word = ""
    else:
        if flag:
            word += char
        else:
            stack.append(char)

print(str.join(" ", answer))       