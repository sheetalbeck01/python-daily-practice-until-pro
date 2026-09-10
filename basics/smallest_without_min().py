# Find the smallest number without using min()

num = [12,8,3,32,1,-1,4,6,23]

smallest = num[0]

for n in num:
    if n < smallest:
        smallest = n

print(smallest)