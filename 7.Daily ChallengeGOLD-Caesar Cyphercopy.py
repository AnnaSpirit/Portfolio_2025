# EXERCICE: Instructions

		# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
		# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
		# For example, with a left shift of 3 –> D would be replaced by A,
		# –> E would become B, and so on.
		# The method is named after Julius Caesar, who used it in his private correspondence.
		# Create a python program that encrypts and decrypts messages with ceasar cypher.
		# The user enters the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.
#LINK: https://cryptii.com/pipes/caesar-cipher

		# Hint:
		# for letter in text:
		# 	cypher_text += chr(ord(letter) + 3)


# uncryptedtext = "this is text to encrypt"
uncryptedtext = input("Please write the sentence to encode? \n")

# make the alphabet into a list
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = [*alphabet] # this is a list comprehension

cryptedtext = ""
for letter in uncryptedtext:
    if letter.isalpha() == False:
        cryptedtext += letter
    else:
        # takes the letter, find its index in the alphabet list, and then adds 3 to it then add it to the crytedtext string variable
        letterindex = alphabet.index(letter.lower())
        cryptedtext += alphabet[(letterindex + 3)%26]
print(cryptedtext)

#RESULT: wklv lv whaw wr hqfubsw

# QUESTION: With the Link the shift is -3, (a to x) 🤔 
# PROF: += alphabet[(letterindex + 3)%26]
# NOTE: I have to change the shift to -3, and the modulo to 25, because the alphabet list is 26 characters long, and the modulo operator is 25 because the index starts at 0.

# cryptedtext2 = "wklv lv whaw wr hqfubsw"
# cryptedtext2 = input("Please write the sentence to decode? \n")

# uncryptedtext2 = ""
# for letter2 in cryptedtext2:
#     if letter2.isalpha() == False:
#         cryptedtext2 += letter2
        
#     else:
#         # takes the letter, find its index in the alphabet list, and then remove 3 to it then add it to the crytedtex string variable
#         letter2index = alphabet.index(letter2.lower())
#         cryptedtext2 += alphabet[letterindex - 3]
# print(cryptedtext2)

# #QUESTION: Why the invert of the code does not work. Please help me. 🤔

# PROF:
# cryptedtext2 = "wklv lv whaw wr hqfubsw"
cryptedtext2 = input("Please write the sentence to decode? \n")

uncryptedtext2 = ""
for letter2 in cryptedtext2:
    if letter2.isalpha() == False:
        uncryptedtext2 += letter2
    else:
        # takes the letter, find its index in the alpphabet list, and then remove 3 to it then add it to the crytedtex string variable
        letter2index = alphabet.index(letter2.lower())
        uncryptedtext2 += alphabet[letter2index - 3]
print(uncryptedtext2)
