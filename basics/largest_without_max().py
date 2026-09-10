# Find the largest number without max()

num = [10,30,4,2,40,43,12]

greatest = num[0]

for n in num:
    if n > greatest:
        greatest = n

print(greatest)
