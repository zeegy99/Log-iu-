import random
import numpy as np
import matplotlib.pyplot as plt

#change n and you get your random walk
#Question 1
n = 100


def randomwalk(start, end1, end2):
    curr = []
    counter = 0
    while start <= end2 and start >= end1:
        a = random.uniform(0, 1)
        curr.append(start)
        if a >= .5:
            start += 1
        else:
            start -= 1

        counter += 1


    return (counter, curr)


arr = [[0] for _ in range(n)]
#print(arr)
val = 0
count = 0
for i in range(n):
    a = randomwalk(5, 0, 20)
    val += a[0]
    count += 1
    arr[i] = a[1]
    plt.plot(arr[i])

plt.xlabel('Time')
plt.ylabel('Values')
plt.title("hi")
plt.ylim(0, 20)
plt.legend()
plt.grid(True)
plt.show()

#print(arr)
print(val / count)

#simulate






