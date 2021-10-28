import random

fails = []
numsum = 0
for i in range(10):
    num = 0
    loops = 0
    while(loops < 2000):
        total = []
        has_num = False
        for i in range(43):
            x = random.randint(0,4)
            total.append(x)
        for i in range(4):
            if total.count(i) == 0:
                has_num = True
        if has_num:
            num += 1
        total.clear()
        loops += 1
    fails.append(num)
    print(loops, num)

for i in fails:
    numsum += i
print(numsum/len(fails) * 100)