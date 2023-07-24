import os
os.system("clear")
print("\n GUNAKAN KONEKSI INTERNET  \n\n")
domain = input("Masukan Domain: ")

os.system(f"python3 knockpy.py  {domain} --no-http-code 404 500 530 -th 10 -o hasil")
print("\n\n  Data disimpan di folder hasil \n\n ")

