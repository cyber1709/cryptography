class RailFence:
    def encrypt(self, plain_text, key):
        encrypted_text = []
        for i in range(key):
            for j in range(i, len(plain_text), key):
                encrypted_text.append(plain_text[j])
        encrypted_text = ''.join(encrypted_text)
        print("Encrypted Text:", encrypted_text)
        return encrypted_text

    def decrypt(self, cipher_text, key):
        # Calculate the length of each rail
        rail_lengths = [len(cipher_text[i::key]) for i in range(key)]
        
        # Prepare rails to store the split cipher text
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(cipher_text[start:start + length])
            start += length
        
        # Reconstruct the plaintext by reading the zigzag pattern
        plain_text = []
        for i in range(len(cipher_text)):
            rail_index = i % key
            plain_text.append(rails[rail_index][0])
            rails[rail_index] = rails[rail_index][1:]  # Remove the used character
        
        # Join and return the plaintext
        plain_text = ''.join(plain_text)
        print("Decrypted Text:", plain_text)
        return plain_text


# Example Usage
obj = RailFence()
encrypted = obj.encrypt("HELLOWORLDINCS", 3)
obj.decrypt(encrypted, 3)
