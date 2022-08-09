# Kyle
# Created 8/8/2022

# module to encrypt and decrypt passwords
from cryptography.fernet import Fernet

# function to initially create the key.key file to store encrypted passwords in write bytes "wb" mode.
'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()'''

# function to read the contents of key.key file in read bytes "rb" mode and close it.
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# calling the load_key() function and Fernet is being passed the key
key = load_key() 
fer = Fernet(key)

# function that will view the passwords.txt file in read mode 'r' and close it, 
# strip the end character so a new line is not displayed at the end of text, 
# splitting the data on each line in the passwords.txt file into two variables "user" and "passw" separated by "|",
# and display the usernames and decrypted passwords to the user.
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "|", "Password:", fer.decrypt(passw.encode()).decode())

# function that will append an account name and password that is input by the user to the end of the password.txt file and close it, 
# encrypt the password, 
# and create a new line at the end of the file.
def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# while loop that asks the user if they want to "view" existing passwords, "add" a new password, or press "q" to quit which will exit the loop.
# anthing other than those three inputs will display "Invalid mode." to the user and the loop will continue. 
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

print("Have a Great Day!")
