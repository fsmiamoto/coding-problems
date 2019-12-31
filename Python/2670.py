people = []
for i in range(3):
    people.append(int(input()))

times = [0, 0, 0]
for i in range(3):
    for j in range(3):
        times[i] += people[j] * 2 * abs(i - j)

print(min(times))
