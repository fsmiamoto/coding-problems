def f_range(lim_inf=0, lim_sup=0, step=1):
    n = lim_inf
    while(n < lim_sup):
        yield n
        n+= step

lista = [1, 2, 3]
for i in f_range(0, 2, .2):
    for n in lista:
        print('I={} J={}'.format(i, n + i))
        
        



