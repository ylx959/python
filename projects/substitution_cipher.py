import random
import string

chars=string.punctuation+string.digits+string.ascii_letters+" "
chars=list(chars)
key=chars.copy() #copy才不會和chars共用同一個list

random.shuffle(key) #打亂後的key就是密碼表

#print(f"chars:{chars}")
#print(f"key:{key}")

#encrypt
plain_text=input("enter a message to encrypt: ")
cypher_text=""

for letter in plain_text:
    index=chars.index(letter) #找到字元的位置，再換成key同位置的字元
    cypher_text+=key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cypher_text}")
#decrypt
cypher_text=input("enter a message to decrypt: ")
plain_text=""

for letter in cypher_text:
    index=key.index(letter) #解密時反過來查
    plain_text+=chars[index]

print(f"original message:{plain_text}")