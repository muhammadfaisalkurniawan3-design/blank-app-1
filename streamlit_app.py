import streamlit as st

st.title("🎈 LPK SUKSES")
import streamlit as st

st.set_page_config(page_title="Analisis Kadar Fe", layout="centered")

st.title("🧪 Penentuan Kadar Fe")

st.write("Menghitung kadar Fe berdasarkan kurva kalibrasi")

# =========================
# INPUT KURVA KALIBRASI
# =========================

st.subheader("Input Persamaan Kalibrasi")

a = st.number_input(
    "Nilai slope (a)",
    value=0.1200,
    format="%.4f"
)

b = st.number_input(
    "Nilai intercept (b)",
    value=0.0050,
    format="%.4f"
)

# =========================
# INPUT ABSORBANSI
# =========================

st.subheader("Input Data Sampel")

absorbansi = st.number_input(
    "Absorbansi Sampel",
    value=0.2500,
    format="%.4f"
)

# =========================
# INPUT BAKU MUTU
# =========================

st.subheader("Baku Mutu")

baku_mutu = st.number_input(
    "Baku Mutu Fe (mg/L)",
    value=1.0,
    format="%.3f"
)

# =========================
# PERHITUNGAN
# =========================

if st.button("Hitung Kadar Fe"):

    # Menghitung konsentrasi
    # x = (y - b) / a

    if a != 0:

        kadar_fe = (absorbansi - b) / a

        st.success(f"Kadar Fe = {kadar_fe:.4f} mg/L")

        # =========================
        # EVALUASI BAKU MUTU
        # =========================

        if kadar_fe <= baku_mutu:
            st.info("✅ Memenuhi baku mutu")

        else:
            st.error("❌ Melebihi baku mutu")

    else:
        st.error("Slope tidak boleh 0")
