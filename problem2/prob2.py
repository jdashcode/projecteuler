x = 0
y = 1
evens = []
while y < 4000000:
    next = x + y
    x = y
    y = next

    if x % 2 == 0:
        evens.append(x)

sum = 0
for num in evens:
    sum += num

print(sum)
