## Cryptography



#### <u>Commonly used Encryption and Decryption Functions</u>

1. **Base64 Encode/Decode**:
   - **Meaning**: Encode binary data into Base64 format, or decode Base64 data into binary form.
   - **Example**: Encoding text to Base64 format: `Hello, World!` -> `SGVsbG8sIFdvcmxkIQ==`
2. **Hex Encode/Decode**:
   - **Meaning**: Encode binary data into hexadecimal form, or decode hexadecimal data into binary form.
   - **Example**: Encoding text to hexadecimal format: `Hello, World!` -> `48656c6c6f2c20576f726c6421`
3. **ROT13 (Rotate by 13 Places)**:
   - **Meaning**: Rotate letters in the text by 13 places in the alphabet. For each letter in the alphabet, move 13 places forward or backward. It can be used for simple encryption and decryption.
   - **Example**: `Hello, World!` -> `Uryyb, Jbeyq!`
4. **AES Encrypt/Decrypt**:
   - **Meaning**: Encrypt and decrypt using the Advanced Encryption Standard. Requires specifying a key and an initialization vector (IV).
   - **Example**: Encrypting text `Hello, World!` using the key `mysecretkey` and IV `1234567890123456`
5. **URL Encode/Decode**:
   - **Meaning**: Encode special characters in the text into URL-safe format, or decode URL-encoded text into original text.
   - **Example**: Encoding text to URL-safe format: `Hello, World!` -> `Hello%2C%20World%21`
6. **Binary Operations**:
   - **Meaning**: Perform binary operations such as AND, OR, XOR, etc., for bitwise manipulation of binary data.
   - **Example**: Performing XOR operation on two binary data.
7. **ASCII Encode/Decode**:
   - **Meaning**: Encode text characters into their ASCII representations, or decode ASCII representations into text characters.
   - **Example**: Encoding text to ASCII representation: `Hello, World!` -> `72 101 108 108 111 44 32 87 111 114 108 100 33`
   - ACSII is abbreviated from **American Standard Code for Information Interchange**, is a [character encoding](https://en.wikipedia.org/wiki/Character_encoding) standard for electronic communication. ASCII codes represent text in computers, [telecommunications equipment](https://en.wikipedia.org/wiki/Telecommunications_equipment), and other devices. Because of technical limitations of computer systems at the time it was invented, ASCII has just 128 [code points](https://en.wikipedia.org/wiki/Code_point), of which only 95 are [printable characters](https://en.wikipedia.org/wiki/ASCII#Printable_characters), which severely limited its scope.

————————————



#### <u>Caesar Cipher</u>

By shifting each letter by a fixed number of positions to encrypt a message. The Caesar Cipher is **<u>not secure**</u> by modern standards:

**Example**: Plaintext: "HELLO" to Ciphertext: "KHOOR", with a right - shift of 3.

**Key Space**: There are only 26 possible shifts, making it **<u>vulnerable to brute force attacks</u>** where an attacker tries all possible shifts.

**Frequency Analysis**: Since it is a substitution cipher, the letter frequency in the ciphertext remains the same as in the plaintext. This makes it susceptible to frequency analysis attacks, where the attacker uses the known frequency of letters in the language to deduce the shift value.

————————————



#### <u>Polyalphabetic Cipher</u>

Choose a Keyword and find the number position of keyword, repeat the keyword to match the length of the plaintext, shift the plaintext by using the number position of the keyword.

**Example**: 

Keyword: `LEMON` (position: 11 4 12 14 13), 

Plaintext: `A T T A C K A T D A W N`

Ciphertext: `L X F O P V E F R N H R` (Shift 11 4 12 14 13 11 4 12 14 13 11 4)

##### Advantages

- **Increased Security**: Polyalphabetic ciphers are more secure than monoalphabetic ciphers because they use multiple substitution alphabets. This makes them resistant to frequency analysis.
- **Complexity**: The use of multiple substitution alphabets increases the complexity of the cipher, making it harder to crack.

##### Limitations

- **Key Management**: The security of a polyalphabetic cipher depends on the secrecy and complexity of the key. If the key is discovered or if it is too short, the cipher can be broken.
- **Pattern Recognition**: If the key is short, repeated patterns in the ciphertext can emerge, which can be exploited to break the cipher using techniques such as the Kasiski examination.

————————————



#### Monoalphabetic Cipher

Create a fixed substitution alphabet that maps each letter of the plaintext alphabet to a unique letter in the ciphertext alphabet. 

e.g., Plaintext Alphabet maps Ciphertext Alphabet: 

```
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
```

```
Z Y X W V U T S R Q P O N M L K J I H G F E D C B A
```

Plaintext: ATTACK AT DAWN would be Ciphertext: ZGGZXP ZG WZDM

**Advantages**

- **Simplicity**: Monoalphabetic ciphers are straightforward to implement and understand.
- **Large Key Space**: The large number of possible keys provides some level of security against brute force attacks.

##### Limitations

- **Frequency Analysis Vulnerability**: The most significant weakness of monoalphabetic ciphers is their susceptibility to frequency analysis. Since the substitution is fixed, the frequency of letters in the ciphertext mirrors the frequency of letters in the plaintext. By analyzing the frequency of letters in the ciphertext and comparing it to the expected frequency in the plaintext language, an attacker can deduce the substitution alphabet.

————————————



#### <u>DES (Data Encryption Standard)</u>

A symmetric key block cipher being **<u>considered insecure today</u>** due to its relatively short key length.

**Block length**: 64 bits, Key length: 56 bits ( with 8 bits for parity)

**Modes of Operation**: ECB, CBC, CFB, OFB, CTR (don't matter)

**Evolution and Replacement**:  3DES, AES

**Strengths**:

- DES was a significant advancement in cryptographic techniques when it was introduced.
- It laid the groundwork for the development of more secure encryption algorithms.

**Weaknesses**:

- **Short Key Length**: The 56-bit key length is vulnerable to brute-force attacks. Modern computing power can break DES encryption relatively quickly.
- **Known Cryptographic Weaknesses**: Advances in cryptanalysis have revealed several vulnerabilities in DES, making it unsuitable for protecting sensitive information.

————————————



#### <u>==AES== (Advanced Encryption Standard)</u>

A symmetric key block cipher algorithm which is widely used in various fields, including <u>e-commerce</u>, <u>network communication</u>, and <u>data storage</u>, due to its high security and excellent performance.

**Key Characteristics**

1. **Symmetric Key Encryption**: AES uses the same key for both encryption and decryption. <u>The sender and receiver must share and protect the security of the key</u>.
2. **Block Cipher**: AES divides data into fixed-size blocks (128 bits) and encrypts each data block.
3. **Key Length**: AES supports various key lengths, including 128-bit, 192-bit, and 256-bit, providing different levels of security.

**<u>Strengths</u>**:

- **High Security**: AES offers robust security with its advanced encryption algorithm and key lengths, resisting various attacks.
- **Efficient Performance**: The algorithm design of AES enables efficient encryption and decryption across various hardware and software platforms, suitable for large-scale data processing.

**Weaknesses**:

- **Unknown Backdoor Risks**: While AES is widely used as a public encryption standard, there may be unknown backdoors or vulnerabilities in its implementations that require regular auditing and updates.

##### <u>Applications of AES</u>

- **Network Security**: AES is extensively used to protect network communications, including Virtual Private Networks (VPNs), Secure Socket Layer/Transport Layer Security (SSL/TLS), and more.
- **Data Storage**: AES is employed to encrypt sensitive data stored on disks, databases, or cloud storage.
- **Mobile Devices**: AES secures data privacy on mobile devices such as smartphones, tablets, etc.

————————————



#### ==XOR== Operation

In XOR operation, two binary inputs are compared bit by bit. The result is true (1) if the bits are different, and false (0) if they are the same. The truth table for XOR operation is as follows:

| Input  A | Input  B | Output (A XOR B) |
| -------- | -------- | ---------------- |
| 0        | 0        | 0                |
| 0        | 1        | 1                |
| 1        | 0        | 1                |
| 1        | 1        | 0                |

<img src="/Users/lianggeliang/Library/Application Support/typora-user-images/image-20240309021126582.png" alt="image-20240309021126582" style="zoom:50%;" />

```
Example： 1011 XOR 1100 -------   0111
```

XOR is widely used in cryptography for encryption and decryption purposes. When XORing data with a secret key, the original data can be securely transformed into ciphertext and then decrypted back using the same key.

If the key is random and is at least as long as the message, the XOR cipher is much more secure than when there is key repetition within a message. When the keystream is generated by a [pseudo-random number generator](https://en.wikipedia.org/wiki/Pseudo-random_number_generator), the result is a [stream cipher](https://en.wikipedia.org/wiki/Stream_cipher). With a key that is [truly random](https://en.wikipedia.org/wiki/Hardware_random_number_generator), the result is a [one-time pad](https://en.wikipedia.org/wiki/One-time_pad), which is [unbreakable in theory](https://en.wikipedia.org/wiki/Information-theoretic_security).

**"Brute forcing XOR"** refers to a method of decrypting a message encrypted using the XOR (exclusive OR) operation by systematically trying all possible keys until the correct one is found. In this context, <u>"brute forcing" means trying every possible combination of key values to decrypt the ciphertext</u>. Since XOR is a symmetric operation, the same key used for encryption can be used for decryption. Therefore, by trying every possible key value and applying it to the ciphertext, one can determine which key successfully decrypts the message, revealing the original plaintext.

————————————



#### ==<u>Public Key Cryptography</u>==

Public key cryptography is a type of encryption technique that uses a <u>pair of keys</u>: **a public key** and **a private key**. Unlike traditional symmetric key encryption above, Astymmetric encryption, aka public key cryptography uses two related but different keys to perform encryption and decryption operations. The well known astymmetric encryption has follows: **RSA(Rivest-Shamir-Adleman), ECC(Elliptic Curve Cryptography), DSA(Digital Signature Algorithm)**

**Example：**

If Alice want to send a secret message to Bob, This is how the ciphertext was generated.

<img src="/Users/lianggeliang/Library/Application Support/typora-user-images/image-20240524004249161.png" alt="image-20240524004249161" style="zoom:50%;" />

```
#### or combining two processes

Alice encrypts with her private key.

Then encrypts again with Bob’s public key.

Bob decrypts with his private key.

Then decrypts with Alice’s public key.
```

​		**Encryption**: The sender uses the recipient's public key to encrypt the message. Anyone with the public key can use it to encrypt messages.

​		**Decryption**: The recipient uses their private key to decrypt the received ciphertext to retrieve the original message. Since only the recipient possesses the private key, only they can decrypt the message.

##### Key Features

- **Security**: The security of public key cryptography is based on mathematical problems such as integer factorization and discrete logarithm problem. Even if the public key is known, it is difficult to derive the private key.
- **Authentication**: Public keys can be used for authentication. Senders can sign messages using their private keys, and recipients can verify the authenticity of the signature using the sender's public key.

##### Applications

- **Secure Communication**: Public key cryptography is widely used in areas such as network communication, email, and online banking to ensure the confidentiality and integrity of data transmission.
- **Digital Signatures**: Used for digital signature verification and authentication, ensuring the origin and integrity of messages.
- **Key Exchange**: Used for securely exchanging symmetric keys to encrypt communications involving large amounts of data.

————————————



#### <u>PGP</u>

Pretty Good Privacy (PGP) is an encryption program that uses *public-key cryptography* to encrypt and digitally sign data. <u>We can put our email address and our name to incorporate the *public-key*</u>.

<img src="/Users/lianggeliang/Library/Application Support/typora-user-images/image-20240524011443796.png" alt="image-20240524011443796" style="zoom:33%;" />

Example would be similar to PKC above, After decrypting the email, Bob can use Alice's public key to verify the signature, ensuring that the email indeed originated from Alice and has not been tampered with during transmission.

**Relationship between PGP and PKC**:

**PGP** is a specific **encryption software**, while **PKC** is an **encryption technique**. Their relationship is similar to that between specific software and a general technology. PGP utilizes techniques from PKC such as public key encryption and digital signatures, but it also offers additional functionalities such as symmetric key encryption and key management.

————————————



#### Hashing

##### Example:

If we have a piece of text: `"Hello, World!"`. After processing it through the hash function, we might get a hash value like `"5a2b8f7d"`. If we make a slight modification to the original text, such as removing the exclamation mark: `"Hello, World"`, and process it through the hash function again, we might get a completely different hash value, like `"e3c9a1b6"`.



<u>Hashing is a process of converting arbitrary-sized data into a fixed-size value,</u> typically called a hash value or hash. A hash function employs a specific algorithm to transform input data into a unique output value, which usually exhibits the following characteristics:

**Fixed Length**: Regardless of the size of input data, the hash function generates a hash value of fixed length.

**Uniqueness**: For a given input, the hash function should produce a unique hash value. Even a difference of one byte in the input data should result in completely different hash values.

**Irreversibility**: It should be practically impossible to derive the original input data from the hash value. In other words, it's not feasible to reconstruct the original input data from its hash value.

**Efficiency**: Hash function computation should be efficient, capable of generating hash values quickly even for large datasets.



##### Common Hash Functions

- **MD5**: Invented by Ron Rivest in 1992, now considered flawed.
- **SHA-2**: Recommended, output sizes include 224, 256, 384, and 512 bits.
- **SHA-3**: Released by NIST in 2015.



##### <u>Hash Functions in Practice</u>

1. **Data Integrity Verification**: Hash functions are widely used to ensure the integrity of data during transmission or storage. By computing the hash value of a piece of data before and after transmission or storage, one can verify if the data has been tampered with or corrupted.
2. **Password Storage**: Hash functions are commonly employed to store passwords securely. Instead of storing plaintext passwords, systems typically store the hash values of passwords. When a user attempts to log in, the system hashes the entered password and compares it with the stored hash value.
3. **Digital Signatures**: Hash functions play a crucial role in digital signatures. In digital signature schemes, a hash of the message is signed with the sender's private key. The recipient can then verify the signature using the sender's public key and ensure the integrity and authenticity of the message.
4. **Data Retrieval**: Hash functions are used in data structures like hash tables to facilitate efficient data retrieval. By computing the hash value of a key, one can quickly locate the corresponding data element in the hash table, leading to fast lookup operations.
5. **Cryptographic Applications**: Hash functions are fundamental building blocks in many cryptographic protocols and algorithms. They are used in key derivation functions, message authentication codes (MACs), and various other cryptographic constructions.



##### Salting in Hashing:

Salting in hashing refers to the practice of adding a random value, known as a "salt," to the input data before it is hashed. This salt value is typically a random sequence of characters or bits.

The purpose of salting is to strengthen the security of hashed data, particularly in the context of password storage. By adding a unique salt to each password before hashing it, even if two users have the same password, their hashed values will be different due to the inclusion of the unique salt. This prevents attackers from using precomputed tables (rainbow tables) to easily crack multiple hashed passwords at once, as they would need to compute separate rainbow tables for each salt value.

Salting also mitigates other types of attacks, such as dictionary attacks and brute force attacks, by increasing the complexity of the hash computation required to guess the original input data.

In summary, salting in hashing is a security measure that adds a random value to input data before hashing it, enhancing the security of hashed data, particularly in password storage scenarios.



##### Different between Hashing and Encryption:

Hashing and encryption are both cryptographic techniques used to secure data, but they serve different purposes and have distinct characteristics:

1. **Purpose**:
   - **Hashing**: The primary purpose of hashing is to generate a fixed-size hash value or digest of input data. Hashing is commonly used for data integrity verification, digital signatures, and password storage.
   - **Encryption**: Encryption is used to transform plaintext data into ciphertext using an encryption algorithm and a secret key. The main purpose of encryption is to protect data confidentiality, ensuring that only authorized parties can access the original plaintext.
2. **Output**:
   - **Hashing**: Hashing produces a fixed-size output known as a hash value or digest. Hash values are unique to the input data and are generally irreversible, meaning it is computationally infeasible to reconstruct the original input from the hash value.
   - **Encryption**: Encryption produces ciphertext, which is the encrypted form of the plaintext data. Ciphertext can be decrypted back to plaintext using the decryption algorithm and the appropriate decryption key.
3. **Reversibility**:
   - **Hashing**: Hashing is generally irreversible. Once data is hashed, it is difficult or impossible to reconstruct the original input from the hash value.
   - **Encryption**: Encryption is reversible, meaning ciphertext can be decrypted back to its original plaintext using the decryption key.
4. **Use Cases**:
   - **Hashing**: Hashing is used for data integrity verification, password hashing, digital signatures, and indexing in data structures like hash tables.
   - **Encryption**: Encryption is used to protect sensitive data during transmission or storage, such as in secure communication protocols, data-at-rest encryption, and secure file transfer.

In summary, hashing is primarily used for data integrity verification and digital signatures, producing irreversible hash values. Encryption, on the other hand, is used for data confidentiality, transforming plaintext into ciphertext using encryption algorithms and keys that allow reversible decryption.

————————————



#### PRNG (pseudo-random number generator)

A pseudo-random number generator (PRNG) is a computer algorithm that produces a sequence of numbers that appear random but are actually deterministic. 

The term "pseudo-random" indicates that while the generated numbers exhibit properties of randomness, they are produced by a deterministic process and are entirely predictable if you know the starting point (seed) of the sequence.  (Emu Casino)

It's important to note that the quality of a PRNG depends on the underlying algorithm and the seed used to initialize it. A good PRNG should produce sequences that pass statistical tests for randomness and have a long period before repeating patterns. 

————————————



#### Digital Signatures

Digital signatures are encrypted tags added to electronic documents or data <u>to verify the source, integrity, and non-repudiation of the document</u> which was proposed by Diffie and Hellman in 1976.

The process of digital signatures includes the following steps:

1. **Hash Calculation**: The signer calculates the hash value of the document using a hash function, generating a unique representation of the document's content.
2. **Private Key Signing**: The signer encrypts the hash value of the document using their private key, generating the digital signature. The private key is the signer's secret key known only to them.
3. **Public Key Verification**: The signer sends the digital signature along with the original document to the recipient. The recipient decrypts the digital signature using the signer's public key to obtain the document's hash value.
4. **Hash Comparison**: The recipient calculates another hash value of the received document using the same hash function. Then, the recipient compares the two hash values. If the hash values match, the document has not been tampered with.
5. **Signature Verification**: If the hash values match, the recipient can confirm the source and integrity of the document. Additionally, the recipient can use the signer's public key to verify the validity of the digital signature, ensuring the signer's identity.



##### Diffie-Hellman Vulnerability

- **Issue**: Vulnerable to man-in-the-middle attacks (MITM).
- **Mitigation**: Use signatures for identity verification.

————————————



#### Key length

| Encryption Method                     | Key Placement                                                | Key Length                            |
| ------------------------------------- | ------------------------------------------------------------ | ------------------------------------- |
| **Symmetric Encryption**              |                                                              |                                       |
| AES                                   | Client, Server, Key Management System                        | 128, 192, 256 bits                    |
| DES                                   | Client, Server, Key Management System                        | 56 bits                               |
| 3DES                                  | Client, Server, Key Management System                        | 112, 168 bits                         |
| Blowfish                              | Client, Server, Key Management System                        | 32–448 bits (commonly 128 bits)       |
| RC4                                   | Client, Server, Key Management System                        | 40–2048 bits                          |
| **Asymmetric Encryption**             |                                                              |                                       |
| RSA                                   | Public Key: Public Directory; Private Key: Client, Server, Secure Hardware Device | 1024, 2048, 4096 bits                 |
| ECC                                   | Public Key: Public Directory; Private Key: Client, Server, Secure Hardware Device | 160-521 bits                          |
| DSA                                   | Public Key: Public Directory; Private Key: Client, Server, Secure Hardware Device | 1024, 2048, 3072 bits                 |
| **Hash Algorithms**                   | No Key Required                                              |                                       |
| MD5                                   | Not Applicable                                               | 128 bits (hash output)                |
| SHA-1                                 | Not Applicable                                               | 160 bits (hash output)                |
| SHA-256                               | Not Applicable                                               | 256 bits (hash output)                |
| SHA-3                                 | Not Applicable                                               | 224, 256, 384, 512 bits (hash output) |
| **Message Authentication Code (MAC)** |                                                              |                                       |
| HMAC (using SHA-256)                  | Client, Server, Key Management System                        | Variable (depends on hash function)   |

————————————



#### ==Possible Questions==

#### Easy

1. **Why salt passwords before hashing?**

   Salting passwords before hashing enhances security by increasing entropy and uniqueness, preventing rainbow table, dictionary, and brute force attacks, enhancing overall security, and avoiding hash collisions.

2. **Are hash functions secure?**

   The security of hash functions <u>depends on various factors</u>, including the specific algorithm used, the length of the hash output, and the context of their application. <u>Generally, well-designed cryptographic hash functions, such as SHA-2 and SHA-3, are considered secure for many practical purposes</u>, exhibiting properties like collision resistance, preimage resistance, and second preimage resistance.

   However, it's essential to note that <u>hash functions can be vulnerable to certain attacks</u>, especially as computational power and cryptanalytic techniques evolve. <u>Older hash functions like MD5 and SHA-1 are now considered weak due to known vulnerabilities, including collision attacks.</u>

3. **Diffie-Hellman key exchange failed, what went wrong?**

   If a Diffie-Hellman key exchange fails, possible issues include:

   1. Using non-prime numbers for parameters.
   2. Mismatched parameters between parties.
   3. Implementation errors in calculations.
   4. Network issues or data corruption.
   5. Man-in-the-middle attacks.
   6. Insufficient randomness in private keys.

   Ensure correct and agreed-upon parameters, proper implementation, secure communication, and adequate randomness to resolve the issue.

4. ##### **how do we make sure the key is shared between the two parties securely?**

   To securely share a key between two parties, you can use:

   1. Diffie-Hellman Key Exchange: Each party generates a public-private key pair, exchanges the public keys, and computes a shared secret key.
   2. Public Key Infrastructure (PKI): One party encrypts the key with the other's public key, and the recipient decrypts it with their private key.
   3. Pre-Shared Keys (PSK): Exchange the key in advance through a secure method.
   4. Key Distribution Centers (KDC): A central authority distributes keys securely to both parties.
   5. Quantum Key Distribution (QKD): Use quantum mechanics to share keys securely.
   6. Secure Communication Channels: Use protocols like TLS to establish a secure channel and then exchange the key.

   Each method ensures the key is shared without being intercepted by unauthorized parties.

   

#### Medium - Hard

1. **When is it safe to use ECB mode?**

   ECB mode is safe to use only when:

   - Encrypting short, independent data blocks.
   - The data is not sensitive.
   - Performance testing or debugging is the primary concern.

   For most applications, it's safer to choose more secure modes like CBC or GCM.

2. **Does n-DES improve security if performance isn't an issue? Why? Any limitations?**

   Using n-DES (multiple iterations of the Data Encryption Standard) can increase security by adding complexity, but it comes with performance overhead and key management challenges. However, it may still be vulnerable to certain attacks, and compatibility issues may arise. In most cases, modern algorithms like AES are preferred for better security and efficiency.

3. **Properties of plaintext to fully utilize the key space with split cipher?**

   For a split cipher to fully utilize the key space, the plaintext should be high in entropy, exhibit uniform distribution, possess independence between its parts, and demonstrate randomness to prevent predictability.

4. **Does adding additional substitution and/or transposition layers improve security?**

   Yes, adding additional substitution and/or transposition layers can enhance security by increasing the complexity of the encryption process, making it more challenging for attackers to decrypt the ciphertext without the correct key.

