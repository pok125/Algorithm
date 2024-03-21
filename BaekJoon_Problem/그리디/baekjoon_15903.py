N, M = map(int, input().split(" "))
cards = list(map(int, input(). split()))

count = 0
while count < M:
    cards.sort()
    hap = cards[0] + cards[1]
    cards[0] = hap
    cards[1] = hap

    count +=1

print(sum(cards))