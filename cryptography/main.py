import getpass
import easygui
import pathlib

from Cryptographer import encrypt, decrypt



def startEncrypt(data, filename):
    failure = ""
    keyword = None
    while True:
        keyword = getpass.getpass(f"{failure}\nplease enter your keyword. This keyword is meant to encrypt and decrypt your data. Please hold on to it as you will not be able to read you encrypted data without your keyword. ")
        password_check = getpass.getpass("Please re-enter your keyword as validation. ")
        if keyword == password_check: break
        failure = "\n Keyword did not match!\n"

    with open(filename, "w") as file:
        extension = encrypt(f"extension={pathlib.Path(filename).suffix}", keyword)
        encrypted_data = encrypt(data, keyword)
        file.write(encrypted_data+extension)

    pathlib.Path(filename).rename(pathlib.Path(filename).with_suffix(".txt"))


def startDecrypt(data, filename):
    keyword = getpass.getpass("Please enter your keyword. This keyword was used to encrypt your data so please provide the same keyword. ")
    with open(filename, "w") as file:
        decrypted_data = decrypt(data, keyword)
        extension_pos = decrypted_data.find("extension=") + 10
        extension = decrypted_data[extension_pos:]
        decrypted_data = decrypted_data.replace(f"extension={extension}", "")

        file.write(decrypted_data)

    p = pathlib.Path(filename)
    p.rename(p.with_suffix(extension))


functions = {
    "encrypt": startEncrypt,
    "decrypt": startDecrypt
}



mode_selected = False
failure = ""
while not mode_selected:
    mode = input(f"{failure}\nWould you like to encrypt or decrypt something? (E/D) ")
    if mode.upper() == "E": mode_selected = "encrypt"
    elif mode.upper() == "D": mode_selected = "decrypt"
    failure = "\nPlease select the encryption or decryption mode by typing E or D"


data = input("What would you like to {}? (press enter to select a file or start typing your text to {}) ".format(mode_selected, mode_selected))
if data == "":
    with open(easygui.fileopenbox()) as file: data = file.read()
functions[mode_selected](data, file.name)
