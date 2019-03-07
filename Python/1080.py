val_pos = [0,0]
for i in range(100):
    n = int(input())
    if n > val_pos[0]:
        val_pos[0] = n
        val_pos[1] = i + 1

print(val_pos[0])
print(val_pos[1])
