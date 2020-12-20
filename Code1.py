n=int(input('Enter no of star you want to print '))

for i in range(n+1):
    for j in range(i):
        print('*',end='')
    print()

for i in range(n+1):
    for j in range(n+1-i):
        print('*',end='')
    print()