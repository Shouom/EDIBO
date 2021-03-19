import random
# value = random.randint(1,10)
# print(value)
x = random.randint(1, 20000)
y = random.randint(1, 20000)
while x < y:
    print(x)
    x += 1
print(x, "x")
print(y, "y")
