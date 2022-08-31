a = []
counter_1 = 0

n = int(input())
m = int(input())

for i in range(n):
    a.append(list())
    for j in range(m):
        numb = int(input())
        a[i].append(numb)
    if 0 not in a[i]:
        counter_1 += 1
    else:
        counter_1 = counter_1

print("Matrix:")
for i in range(n):
    print(a[i])
print("Haven't 0:", counter_1)