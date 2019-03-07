sal = float(input())
if sal <= 2000:
    print('Isento')
elif sal <= 3000:
    print('R$ {:.2f}'.format((sal - 2000) * 0.08))
elif sal <= 4500:
    print('R$ {:.2f}'.format((sal - 3000) * 0.18 + 80))
else:
    print('R$ {:.2f}'.format((sal - 4500) * 0.28 + 270 + 80))
