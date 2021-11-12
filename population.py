population = int(input('starting amount of organisms: '))
growth = int(input('average daily growth in persents: '))
day = int(input('amount of days for reproduction: '))
print ('day', 'population')
print(1, '  ', population)
n = 1
while n != day:
    n += 1
    population += population * growth * 0.01
    print(n, '  ', population)