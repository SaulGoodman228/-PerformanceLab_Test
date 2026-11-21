n,m = int(input()), int(input())

steps = list()

step = 0
k = 0
while k!=1:
    step += m-1
    k = 1+step//n
    steps.append(step)

print(steps)