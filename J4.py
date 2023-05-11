n = int(input())
	
row1 = input().split()
row2 = input().split()
		
total = 0 

for a in range(n):
	if row1[a] == "1":
		total += 3
	if (row2[a] == "1")
		total += 3
		
for a in range(n-1):
	if row1[a] == "1" and row1[a+1] == "1":
		total -= 2
	if row2[a] == "1" and row2[a+1] == "1":
		total -= 2
		
		
for a in range(0, n, 2):
	if row1[a] == "1" and row2[a] == "1":
		total -= 2

print(total)
