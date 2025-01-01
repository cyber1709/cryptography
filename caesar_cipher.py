alphabet_dict = {chr(i): i - 97 for i in range(97, 123)}
reverse_alphabet_dict = {i - 97: chr(i) for i in range(97, 123)}

class Caesar_Cipher:
    def __init__(self):
        pass
    
    def encrypt(self, plain_text, key):
        cipher_text = []
        print("Plain Text:", plain_text)
        for item in plain_text:
            if item.isalpha():
                value = alphabet_dict[item]
                encypted_value = (value + key) % 26
                cipher_text.append(reverse_alphabet_dict[encypted_value])
            else:
                cipher_text.append(item)
        cipher_text = "".join(cipher_text)
        print("Cipher Text:",cipher_text)
        return cipher_text
    
    def decrypt(self, cipher_text, key):
        plain_text = []
        print("Cipher Text:", cipher_text)
        for item in cipher_text:
            if item.isalpha():
                value = alphabet_dict[item]
                decrypted_value = (value - key) % 26
                plain_text.append(reverse_alphabet_dict[decrypted_value])
            else:
                plain_text.append(item)
        plain_text = ''.join(plain_text)
        print("Plain Text:", plain_text)
        return plain_text
            

obj = Caesar_Cipher()
obj.encrypt('gaurav arora dob 17', 6)
print("===========================")
obj.decrypt('mgaxgb gxuxg juh 17', 6)
