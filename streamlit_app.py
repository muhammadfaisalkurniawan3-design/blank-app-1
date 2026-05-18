import streamlit as st

st.title("🎈 LPK SUKSES")
import streamlit as st
import random

# Inisialisasi angka rahasia
if "angka_rahasia" not in st.session_state:
    st.session_state.angka_rahasia = random.randint(1, 100)

if "jumlah_tebakan" not in st.session_state:
    st.session_state.jumlah_tebakan = 0

st.title("🎮 Game Tebak Angka")

st.write("Saya memilih angka antara 1 sampai 100")

# Input tebakan
tebakan = st.number_input(
    "Masukkan tebakan kamu:",
    min_value=1,
    max_value=100,
    step=1
)

# Tombol cek
if st.button("Tebak"):

    st.session_state.jumlah_tebakan += 1

    if tebakan < st.session_state.angka_rahasia:
        st.warning("Terlalu kecil!")

    elif tebakan > st.session_state.angka_rahasia:
        st.warning("Terlalu besar!")

    else:
        st.success(
            f"🎉 Benar! Angkanya adalah {st.session_state.angka_rahasia}"
        )

        st.info(
            f"Kamu menebak dalam "
            f"{st.session_state.jumlah_tebakan} percobaan"
        )

# Tombol reset
if st.button("Main Lagi"):

    st.session_state.angka_rahasia = random.randint(1, 100)
    st.session_state.jumlah_tebakan = 0

    st.rerun()
