def normalisasi_nama(nama):
    # Menghapus spasi ekstra dan membuat Title Case
    return " ".join(nama.split()).title()

def buat_inisial(nama):
    # Mengambil huruf pertama dari setiap kata
    return "".join(k[0].upper() for k in nama.split())

def normalisasi_kode(kode):
    # Mengubah spasi menjadi tanda hubung (-) dan membuat UPPERCASE
    return "-".join(kode.split()).upper()

# --- Input dari User ---
nama_input = input("Nama: ")
kode_input = input("Kode kelas: ")

# --- Proses ---
nama_bersih = normalisasi_nama(nama_input)
kode_kelas = normalisasi_kode(kode_input)
jumlah_kata = len(nama_bersih.split())
inisial = buat_inisial(nama_input)

# --- Output ---
print("\nContoh Output")
print(f"Nama bersih : {nama_bersih}")
print(f"Kode kelas  : {kode_kelas}")
print(f"Jumlah kata : {jumlah_kata}")
print(f"Inisial     : {inisial}")