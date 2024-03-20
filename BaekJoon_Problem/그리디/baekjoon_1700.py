import sys

N, K = map(int, sys.stdin.readline().split(" "))
# products = list(map(int, sys.stdin.readline().split(" ")))
# use_queue = [products[i] for i in range(N)]
# wait_queue = [products[i] for i in range(N, N + N)]
# count = 0

elec_list = list(map(int, input().split()))
plug = set()
cnt = 0

def find_latest(idx) :
  result = 0
  max_idx = -1
  for num in plug :
    try :
      num_idx = elec_list[idx:].index(num)
    except :
      num_idx = K
    if max_idx < num_idx :
      result, max_idx = num, num_idx
  
  return result
  
for idx, num in enumerate(elec_list) :
  plug.add(num)
  if len(plug) > N :
    cnt += 1
    latest_used = find_latest(idx)
    plug.discard(latest_used)

print(cnt)