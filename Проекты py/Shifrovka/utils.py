def caesar_cipher(text, shift, mode='encrypt'):
    result = []
    shift_val = shift if mode == 'encrypt' else -shift

    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
            shifted_char = chr((ord(char) - start + shift_val) % 26 + start)
            result.append(shifted_char)
        elif 'A' <= char <= 'Z':
            start = ord('A')
            shifted_char = chr((ord(char) - start + shift_val) % 26 + start)
            result.append(shifted_char)
        else:
            result.append(char) # Оставляем небуквенные символы без изменений
    return "".join(result)

def atbash_cipher(text, mode='encrypt'):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            shifted_char = chr(ord('a') + (ord('z') - ord(char)))
            result.append(shifted_char)
        elif 'A' <= char <= 'Z':
            shifted_char = chr(ord('A') + (ord('Z') - ord(char)))
            result.append(shifted_char)
        else:
            result.append(char)
    return "".join(result)
def affine_cipher_caesar(text, a, b, mode='encrypt'):
    result = []

    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
            if mode == 'encrypt':
                shifted_char = chr((a * (ord(char) - start) + b) % 26 + start)
            elif mode == 'decrypt':
                a_inv = -1
                for i in range(26):
                    if (a * i) % 26 == 1:
                        a_inv = i
                        break

                if a_inv == -1:
                    return "Ошибка: 'a' должно быть взаимно простым с 26 для дешифрования."

                shifted_char = chr((a_inv * (ord(char) - start - b + 26)) % 26 + start) # +26 для корректной работы с отрицательными числами
            result.append(shifted_char)
        elif 'A' <= char <= 'Z':
            start = ord('A')
            if mode == 'encrypt':
                shifted_char = chr((a * (ord(char) - start) + b) % 26 + start)
            elif mode == 'decrypt':
                a_inv = -1
                for i in range(26):
                    if (a * i) % 26 == 1:
                        a_inv = i
                        break

                if a_inv == -1:
                    return "Ошибка: 'a' должно быть взаимно простым с 26 для дешифрования."

                shifted_char = chr((a_inv * (ord(char) - start - b + 26)) % 26 + start)
            result.append(shifted_char)
        else:
            result.append(char) # Оставляем небуквенные символы без изменений
    return "".join(result)
