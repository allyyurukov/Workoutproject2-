# Workoutproject2- 
To encrypt or decrypt a text file in this project, a simple transposition cipher has been used. A transposition cipher basically mixes up the characters of the plain text so that it is difficult to understand without the required key.
There are two modes of executing the program either to encrypt or to decrypt.
Encrypt a file:
      python wp2.py -e inputfile.txt encryptedfile.txt key
Decrypt a file:
      python wp2.py -d encryptedfile.txt decryptedfile.txt key
It is mandatory for the string “key” to be a positive integer.
wp2.py: This is a root script that manages either encryption or decryption activities.
key_validation.py: It has in it the capability to validating the key for encryption.
transposition_cipher.py: Realizes transposition cipher approach. 
This project follows PEP8 coding standards and includes exception handling and modular code structure for maintainability and scalability.
