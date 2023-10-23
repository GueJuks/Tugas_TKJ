def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:
                shifted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') - shift_amount + 26) % 26) + ord('a'))
            else:
                shifted_char = chr(((ord(char) - ord('A') - shift_amount + 26) % 26) + ord('A'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

while True:
    choice = input("Apakah Anda ingin mengenkripsi (E), mendekripsi (D), atau keluar (Q)? ").upper()

    if choice == 'E':
        plaintext = input("Masukkan pesan yang ingin dienkripsi: ")
        shift = int(input("Masukkan jumlah pergeseran: "))
        encrypted_text = encrypt(plaintext, shift)
        print("Pesan Terenkripsi: ", encrypted_text)
    elif choice == 'D':
        encrypted_text = input("Masukkan pesan yang ingin didekripsi: ")
        shift = int(input("Masukkan jumlah pergeseran: "))
        decrypted_text = decrypt(encrypted_text, shift)
        print("Pesan Terdekripsi: ", decrypted_text)
    elif choice == 'Q':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan 'E', 'D', atau 'Q' (untuk keluar).")
