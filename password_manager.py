from cryptography.fernet import Fernet

print("Welcome to password manager.")

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
def load_key():
   file = open("key.key", "rb")
   key = file.read()
   file.close()
   return key

master_password = input("What is the master password? ")

key = load_key + master_password.encode()
fer = Fernet(key)


#functions

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.strip()
            user, passw = data.split("|")
            print("User:",user, "| Password:", str(fer.decrypt(passw.encode()).decode()))
    

def add():
    name = input("Name: ")
    password = input("Password: ")
    
    with open("password.txt", "a") as f:
        f.write(name + "|" + password + str(fer.encrypt(password.encode())) + "\n")



while True:
    
    mode = input("Would you like to add a new password or add view one (view/add), press q to quit? ").lower()

    if mode == "q":
        break
    
    if mode == "view":
        view()

    elif mode == "add":
        add()
    else:
        print("Invalid mode");
        break
    