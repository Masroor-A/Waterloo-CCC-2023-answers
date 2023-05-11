n = int(input())
days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]
counts = [0] * 5  

for i in range(n):
  availability = input().strip()
  for j in range(5):
    if availability[j] == "Y":
      counts[j] += 1  

max_count = max(counts)
max_days = [str(d+1) for d in range(5) if counts[d] == max_count]

print(",".join(max_days))
