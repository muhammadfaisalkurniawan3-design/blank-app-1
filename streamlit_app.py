import streamlit as st

st.title("🎈 JUAL ACA BELI LELE")
import streamlit as st

# Judul aplikasi
st.title("Kalkulator Sederhana")

# Input angka
angka1 = st.number_input("Masukkan angka pertama", value=0.0)
angka2 = st.number_input("Masukkan angka kedua", value=0.0)

# Pilihan operasi
operasi = st.selectbox(
    "Pilih operasi",
    ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"]
)

# Tombol hitung
if st.button("Hitung"):

    if operasi == "Penjumlahan":
        hasil = angka1 + angka2

    elif operasi == "Pengurangan":
        hasil = angka1 - angka2

    elif operasi == "Perkalian":
        hasil = angka1 * angka2

    elif operasi == "Pembagian":
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            hasil = "Error! Tidak bisa dibagi 0"

    st.success(f"Hasil: {hasil}")
