datas = []
for _ in range(2):
    dia = int(input().split(' ')[1])
    h, m, s = (int(x.strip()) for x in input().split(':')) # Splita no : e depois remove os whitespaces com strip pra entao converter para int.
    datas.append([s,m,h,dia])

d1, d2 = datas
dif = []

for i in range(4):
    if d2[i] >= d1[i]:
        dif.append(d2[i]-d1[i])
    elif i < 2: 
        d2[i+1] -= 1
        dif.append(d2[i] - d1[i] + 60)
    else:
        d2[i+1] -= 1
        dif.append(d2[i] - d1[i] + 24)

total_seg = dif[0] + 60*dif[1] + 60*60*dif[2] + 24*60*60*dif[3]

if total_seg >= 60:
    print('{} dias(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dif[3],dif[2],dif[1],dif[0]))
else:
    print('{} dias(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dif[3],dif[2],1,0))
