from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key().decode()
    print("Generated key:", key)

if __name__ == "__main__":
    generate_key()
