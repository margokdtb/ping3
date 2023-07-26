import re

print("\n\n Isi dulu file sumber_pcapdroid.txt \n\n")

# Konfirmasi dari pengguna
konfirmasi = input("Sudah mengisi? (y/n) ")

if konfirmasi.lower() == 'y':
    # Membaca file input_lama.txt dan mengambil subdomain
    with open('sumber_pcapdroid.txt', 'r') as file:
        data = file.read()
        subdomains = re.findall(r'\b(?:[A-Za-z0-9]+\.)+[A-Za-z]{2,}\b', data)
    
    # Menggunakan set untuk membuat host yang unik
    unique_hosts = set(subdomains)

    # Menyimpan host yang unik dalam file subdomain.txt
    with open('subdomain.txt', 'w') as file:
        for host in unique_hosts:
            file.write(host + '\n')
            
    #import os
    #os.system("python unik3.py")

    print('\n Data disimpan di folder hasil')

else:
    print("\n Pastikan untuk mengisi file sumber_pcapdroid.txt sebelum menjalankan program ini.")
   
# copy file ke folder hasil
import os
import shutil
import datetime

# Tentukan path file asal dan tujuan
file_asal = 'subdomain.txt'
folder_tujuan = 'hasil'

# Mendapatkan tanggal saat ini dalam format YYYY-MM-DD
tanggal_sekarang = datetime.datetime.now().strftime('%Y-%m-%d')

# Mendapatkan nama file tujuan dengan menambahkan tanggal
nama_file_tujuan = f'sumber_pcapdroid_{tanggal_sekarang}.txt'

# Cek jika folder tujuan belum ada, maka buat folder tersebut
if not os.path.exists(folder_tujuan):
    os.makedirs(folder_tujuan)

# Copy file ke folder tujuan dengan nama yang baru
shutil.copy(file_asal, os.path.join(folder_tujuan, nama_file_tujuan))
