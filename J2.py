runs = int(input())
total = 0


pepers = {"Poblano":1500, "Mirasol": 6000, "Serrano": 15500, "Cayenne": 40000, "Thai": 75000, "Habanero": 125000}

for i in range(runs):
	total += pepers[input()]


print(total)
