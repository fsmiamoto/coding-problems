num_of_tests = int(input())

for _ in range(num_of_tests):
    msg = input()
    crypt_msg = []

    for idx, char in enumerate(msg):
        ascii = ord(char)
        if char.isalpha():
            ascii += 3
        if idx < len(msg)/2:
            ascii -= 1
        crypt_msg.append(chr(ascii))

    crypt_msg.reverse()

    print(''.join(crypt_msg))
