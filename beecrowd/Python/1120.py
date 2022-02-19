# 1120 - Revisão do Contrato

while True:
    faulty_digit, ammount = input().split(' ')

    if faulty_digit == '0' and ammount == '0':
        break

    if ammount.find(faulty_digit) == -1:
        print(ammount)
        continue

    filtered_ammount = ammount.replace(faulty_digit, '')

    if filtered_ammount == '':
        print(0)
        continue

    print(int(filtered_ammount))
