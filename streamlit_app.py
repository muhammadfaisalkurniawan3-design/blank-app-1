import streamlit as st

st.title("🎈 LPK SUKSES")
import streamlit as st

st.set_page_config(
    page_title="Analisis Vitamin C",
    layout="centered"
)

st.title("🍊 Penentuan Kadar Vitamin C")

st.write(
    "Menghitung kadar Vitamin C dalam sampel minuman "
    "menggunakan kurva kalibrasi"
)

# =====================================
# INPUT KURVA KALIBRASI
# =====================================

st.header("1. Persamaan Kalibrasi")

a = st.number_input(
    "Slope (a)",
    value=0.0850,
    format="%.4f"
)

b = st.number_input(
    "Intercept (b)",
    value=0.0020,
    format="%.4f"
)

# =====================================
# INPUT ABSORBANSI
# =====================================

st.header("2. Data Sampel")

absorbansi = st.number_input(
    "Absorbansi Sampel",
    value=0.3500,
    format="%.4f"
)

# =====================================
# FAKTOR PENGENCERAN
# =====================================

st.header("3. Faktor Pengenceran")

fp = st.number_input(
    "Faktor Pengenceran",
    value=1.0,
    format="%.2f"
)

# =====================================
# STANDAR / LABEL PRODUK
# =====================================

st.header("4. Standar Vitamin C")

standar = st.number_input(
    "Kadar pada label (mg/L)",
    value=40.0,
    format="%.2f"
)

# =====================================
# PERHITUNGAN
# =====================================

if st.button("Hitung Kadar Vitamin C"):

    if a != 0:

        # Hitung konsentrasi
        konsentrasi = ((absorbansi - b) / a) * fp

        st.success(
            f"Kadar Vitamin C = {konsentrasi:.2f} mg/L"
        )

        # =====================================
        # PERBANDINGAN DENGAN LABEL
        # =====================================

        selisih = konsentrasi - standar

        st.subheader("Perbandingan dengan Label")

        st.write(f"Standar/Label : {standar:.2f} mg/L")
        st.write(f"Hasil Analisis : {konsentrasi:.2f} mg/L")
        st.write(f"Selisih : {selisih:.2f} mg/L")

        if konsentrasi >= standar:
            st.info("✅ Sesuai / di atas standar")
        else:
            st.warning("⚠️ Di bawah standar")

    else:
        st.error("Slope tidak boleh nol")
