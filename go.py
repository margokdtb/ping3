import os
os.system("clear")

print("\n\n SCAN BUG SSLCDN DAN SNI  \n\n")
print("\nPowered by margokdtb@gmail.com Juli 2023  \n")

import os

def display_menu():
    print("Menu:")
    print("1. Cari Sub Domain (Koneksi Internet) ")
    print("2. Convert Hasil")
    print("3. Scan WS dan WS SSL (Koneksi paket data)")
    print("4. Scan SNI  ")
    print("5. Ping SNI  ")
    print("6. Sumber PCAPdroid (isi sumber_pcapdroid.txt) ")
       
    print("0. Keluar")

def run_file(file_number):
    if file_number == 1:
        os.system("python3 k_subdomain1.py")
    elif file_number == 2:
        os.system("python3 k_subdomain2.py")
    elif file_number == 3:
        os.system("python3 ws.py")
    elif file_number == 4:
        os.system("python3 sni1.py")
    elif file_number == 5:
        os.system("python3 sni2.py")
        
    elif file_number == 6:
        os.system("python3 datalama.py")    
         
        
    
                 
        
    elif file_number == 0:
        return
    else:
        print("Pilihan tidak valid")

while True:
    display_menu()
    try:
        choice = int(input("Masukkan pilihan : "))
        run_file(choice)
        if choice == 0:
            break
    except ValueError:
        print("Pilihan tidak valid. Masukkan angka.")
    
    input("Tekan enter untuk melanjutkan...")