strs = []

for _ in range(3):
    strs.append(input())

print('{}{}{}'.format(strs[0],strs[1],strs[2]))
print('{}{}{}'.format(strs[1],strs[2],strs[0]))
print('{}{}{}'.format(strs[2],strs[0],strs[1]))
print('{}{}{}'.format(strs[0][:10],strs[1][:10],strs[2][:10]))
