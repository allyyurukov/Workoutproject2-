import sys
from key_validation import validate_key
from transposition_cipher import encrypt, decrypt

def main():
    if len(sys.argv) != 5:
        print("Usage: python wp2.py -e|-d input_file output_file key")
        sys.exit(1)

    mode, input_file, output_file, key = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])

    try:
        validate_key(key, input_file)
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)

    if mode == '-e':
        encrypt(input_file, output_file, key)
    elif mode == "-d":
        decrypt(input_file, output_file, key)
    else:
        print("Invalid mode")
        sys.exit(1)

if __name__ == "__main__":
    main()