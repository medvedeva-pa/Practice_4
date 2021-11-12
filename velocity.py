velocity = int(input('What is the velocity of vehicle??: '))
hours = int(input('How many hours did it move?: '))
n = 0 
print('Hour', 'Distance')
while n != hours:
    n += 1
    print(n, '  ', velocity * n)
    