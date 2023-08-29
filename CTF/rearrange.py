def decode_string(encoded_string, key):
    decoded_string = ''
    for char in encoded_string:
        if char in key:
            decoded_string += key[char]
        else:
            decoded_string += char
    return decoded_string

# Update the key with the legend/key provided. 
key = {
    'd': 'a', 'k': 'b', 'Z': 'c', 'a': 'd', 'i': 'e', 'N': 'f', 'O': 'g', 'F': 'h', 'G': 'i', 
    'S': 'j', 'v': 'k', 'r': 'l', '}': 'm', 'R': 'n', 'Q': 'o', 'c': 'p', 'q': 'q', 'x': 'r', 
    's': 's', 'g': 't', 'E': 'u', 'n': 'v', 'T': 'w', 'm': 'x', 'V': 'y', 'b': 'z', 'w': 'A', 
    'D': 'B', 'A': 'C', 'H': 'D', 'o': 'E', 'K': 'F', 'e': 'G', '{': 'H', 'Y': 'I', 'z': 'J', 
    'X': 'K', 'u': 'L', 'U': 'M', 'p': 'N', 'P': 'O', 'j': 'P', 'L': 'Q', 'C': 'R', 'I': 'S', 
    'h': 'T', 'J': 'U', 'B': 'V', 'y': 'W', 'M': 'X', 'W': 'Y', 't': 'Z', 'l': '{', 'f': '}'
}

encoded_string = input("Enter the encoded string: ")
decoded_string = decode_string(encoded_string, key)
print("Decoded string:", decoded_string)
