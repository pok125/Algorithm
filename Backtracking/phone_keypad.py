num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
char = ["", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
mapping_phone_num = dict(zip(num, char))
input_num = [2, 5, 9]
answer = []

def solution(index, letter):
    if index >= len(input_num):
        answer.append(letter)
        return
    
    number = input_num[index]
    charaters = mapping_phone_num[number]
    index += 1
    for char in charaters:
        next_letter = letter + char
        solution(index, next_letter
        )

solution(0, "")
print(answer)