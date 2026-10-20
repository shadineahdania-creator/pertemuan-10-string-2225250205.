teks = " belajar python untuk pendidikan "
teks = teks.strip()

# Perbaikan: menggunakan dua spasi ("  ") pada while dan replace 
# agar tidak terjadi perulangan tanpa henti (infinite loop)
while "  " in teks:
    teks = teks.replace("  ", " ")

print(teks.capitalize())