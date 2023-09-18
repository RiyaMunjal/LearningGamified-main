import random


def is_prime(num):

    if num <= 1:
        return False

    if num == 2:
        return True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def generate_prime(bits):

    while True:
        num = random.getrandbits(bits)
        num |= 1
        if is_prime(num):
            return num


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)

    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)


def mod_inv(a, m):
    g, x, y = egcd(a, m)

    if g != 1:
        raise Exception('modular inverse does not exist')

    return x % m


def generate_key_pair():
    p = generate_prime(32)
    q = generate_prime(32)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    d = mod_inv(e, phi)

    return ((e, n), (d, n))


def encrypt(plaintext, public_key):

    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]

    return ciphertext


def decrypt(ciphertext, private_key):

    d, n = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]

    return ''.join(plaintext)


if __name__ == '__main__':
    public_key, private_key = generate_key_pair()
    message = input('Enter message to be coded: ')
    ciphertext = encrypt(message, public_key)
    plaintext = decrypt(ciphertext, private_key)
    print('Original message:', message)
    print('Encrypted message:', ciphertext)
    print('Decrypted message:', plaintext)


def getEncryptedAndDecryptedMessage(message):

    public_key, private_key = generate_key_pair()

    ciphertext = encrypt(message, public_key)
    plaintext = decrypt(ciphertext, private_key)

    return ciphertext, plaintext, public_key, private_key
