from cryptography.fernet import Fernet


def load_key():
    file= open("key.key","rb")
    key =file.read()
    file.cloase()
    return key

mstr_pwd = input("What is the password?")

key = load_key() + mstr_pwd.encode()
fer =Fernet(key)

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key.file.write(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("::")
            print("User: ", user, " password ",  fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + " :: " + fer.encrypt(pwd.encode()).decode()+ "\n")


while True:
    mode = input("Would you like to add new password or view existing password (view/add) , press q to quit").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode! ")
        continue
