from cipher import encrypt, decrypt

def main():
    print("=== Caesar Cipher ===")
    while True:
        choice = input("Choose an option: (E)ncrypt, (D)ecrypt, (Q)uit: ").strip().upper()
        if choice == 'Q':
            print("Exiting...")
            break
        elif choice not in ['E', 'D']:
            print("Invalid option. Please choose E, D, or Q.")
            continue

        message = input("Enter the message: ")
        try:
            shift = int(input("Enter the shift value (integer): "))
        except ValueError:
            print("Invalid shift value. Must be an integer.")
            continue

        if choice == 'E':
            result = encrypt(message, shift)
            print("Encrypted message:", result)
        else:
            result = decrypt(message, shift)
            print("Decrypted message:", result)
        print()

if __name__ == "__main__":
    main()
