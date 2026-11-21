n,m = int(input()), int(input())

steps = [1]

step = m
while step % n != 1:
    steps.append(step%n if step%n!=0 else n)
    step = (step + m-1)%n

print(steps)