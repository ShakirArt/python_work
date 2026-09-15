a = [1, 2, 3, 4, 5, 2, 6, 3, 2., 7, 8, 9, 1, 2, 3]
counts = {}

for i in a:
    counts[i] = counts.get(i,0) + 1
for k, v in counts.items():
    if v > 1:
        print(k,":", v)
