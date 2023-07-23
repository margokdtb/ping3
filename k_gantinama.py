import os
import shutil

# Menampilkan isi folder
def list_files(folder):
    print("Isi folder:")
    for filename in os.listdir(folder):
        print(filename)

# Memilih file untuk dicopy dan diganti namanya
def copy_and_rename_file(source_folder):
    files = os.listdir(source_folder)
    print("\nDaftar file:")
    for i, filename in enumerate(files):
        print(f"{i+1}. {filename}")
    choice = input("Pilih nomor file yang akan dicopy dan diganti namanya: ")

    try:
        index = int(choice) - 1
        old_filename = files[index]
        new_filename = "sumber_knock.txt"
        shutil.copy(os.path.join(source_folder, old_filename), os.path.join(source_folder, new_filename))
        print(f"\nFile {old_filename} telah dicopy dan diganti namanya menjadi sumber_knock.txt")
    except (ValueError, FileNotFoundError, IndexError):
        print("\nPilihan file tidak valid")

# Main program
folder_path = "hasil"  # Ubah menjadi "hasil" jika menggunakan folder "hasil"
#list_files(folder_path)
copy_and_rename_file(folder_path)

#salin file
import os
import shutil

# Pindahkan file sumber_knock.txt ke folder sebelumnya
def move_file(source_folder, destination_folder):
    source_file = os.path.join(source_folder, "sumber_knock.txt")
    destination_file = os.path.join(destination_folder, "sumber_knock.txt")
    
    try:
        shutil.move(source_file, destination_file)
        print("File sumber_knock.txt telah dipindahkan ke folder sebelumnya.")
    except FileNotFoundError:
        print("File sumber_knock.txt tidak ditemukan.")
    except shutil.Error:
        print("File sumber_knock.txt sudah ada di folder sebelumnya.")
        
# Main program
source_folder = "hasil"  # Ganti dengan path folder 'hasil', jika berbeda
destination_folder = os.path.dirname(os.path.abspath(source_folder))

move_file(source_folder, destination_folder)