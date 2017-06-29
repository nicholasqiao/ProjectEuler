sum = 2
current = 3
previous = 2

while current < 4000000:
    next = current + previous
    previous = current
    current = next
    
    if (current%2 == 0):
        sum += current

print sum