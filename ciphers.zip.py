from pwn import xor 

c1 = bytes.fromhex('2E0A193C0802117F0007451C3F23')
c2 = bytes.fromhex('1F0314381C37440D2B5B0B3C191C090D5E4531385E4100321D0B22')


crib_drag = input("enter your text: ")              #if you type welcome to CTF, it is clear that the key is You_got_the_key
crib_drag = crib_drag.encode('UTF-8')  

key = xor(crib_drag,c1)    
key_in_str = key.decode('utf-8')  + "y"             # So adding a "y" to the key
print("The key is : ", key_in_str)
new_key = key_in_str.encode('UTF-8')


flag = xor(c2,new_key)
print ("The decrypted text is:",flag)
