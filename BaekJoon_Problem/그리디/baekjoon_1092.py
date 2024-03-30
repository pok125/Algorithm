import sys

N = int(sys.stdin.readline())
cranes = list(map(int, sys.stdin.readline().split(" ")))
M = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().split(" ")))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
else:
    answer = 0
    while boxes:
       for crane in cranes:
          if boxes and boxes[-1] > crane:
             continue
          for box in boxes:
             if box <= crane:
                boxes.remove(box)
                break
       answer += 1
    
    print(answer)