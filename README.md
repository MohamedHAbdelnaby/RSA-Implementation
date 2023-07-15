# RSA Encryption Algorithm - Python
This repository contains a Python implementation of the RSA encryption and decryption process.

# Description
RSA is a widely-used cryptosystem for secure data transmission. It's a public key cryptosystem for both encryption and authentication and it was invented by Ron Rivest, Adi Shamir, and Leonard Adleman in 1977, hence the name RSA.

The Python program in this repository demonstrates how to generate public and private keys, encrypt a plaintext message, and decrypt a ciphertext message using the RSA algorithm.

The program starts with two prime numbers, p and q, and generates the public and private keys. It then takes a plaintext message, encrypts it using the public key, and finally decrypts the ciphertext back into the original plaintext using the private key.

# Encryption Steps

Here are the steps carried out by the program:

1-  We select two prime numbers, p and q. In our case, p=41 and q=97.

2- We calculate n=p*q.

3- We calculate the Carmichael’s totient function λ(n) = lcm(p-1, q-1).

4- We select a number e, 1 < e < λ(n), such that gcd(e, λ(n)) = 1. In our case, e=13.

5- The public key is then (e, n).

6- To encrypt a plaintext message m, we calculate c = m^e mod n, where m is the numerical equivalent of the plaintext.

# Decryption Steps

1- We calculate d such that ed ≡ 1 mod λ(n). This is our private key.

2- The private key is (d, n).

3- To decrypt the ciphertext, we calculate m = c^d mod n.

# License
This project is licensed under the MIT License - see the LICENSE.md file for details.

# Acknowledgments
This project is purely educational and meant to demonstrate how RSA works at a basic level.
