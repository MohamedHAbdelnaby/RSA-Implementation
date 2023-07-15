# -*- coding: utf-8 -*-
"""RSA_Algorithm_Research_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jabgcao8E16vu03dvzE1ZasENcYXdJZi
"""

import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_euclidean(e, phi):
    if e == 0:
        return (phi, 0, 1)
    else:
        g, x, y = extended_euclidean(phi % e, e)
        return (g, y - (phi // e) * x, x)

def multiplicative_inverse(e, phi):
    _, x, _ = extended_euclidean(e, phi)
    return x % phi

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    p = 41
    q = 97
    n = p * q
    phi = (p-1) * (q-1)

    e = 13
    g = gcd(e, phi)
    while g != 1:
        e = e + 1
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    public = (e, n)
    private = (d, n)

    encrypted_msg = encrypt(public, 'c')  # 'c' = 3
    print('Encrypted:', encrypted_msg)

    decrypted_msg = decrypt(private, encrypted_msg)
    print('Decrypted:', decrypted_msg)