import streamlit as st

st.title("Sistem Rekomendasi Jurusan")
st.write("Praktikum 2 Sistem Cerdas | Ryan - 2313010608, Johan - 2313010604, Angga - 2313010605")

minat = st.selectbox(
    "Minat :",
    ["Matematika", "Kimia", "Fisika", "Sosial", "Bahasa", "Seni", "Teknologi", "Bisnis", "Olahraga"]
)

nilai = st.selectbox(
    "Nilai :",
    ["Tinggi", "Sedang", "Rendah"]
)

hobi = st.selectbox(
    "Hobi :",
    ["Menghitung", "Membaca", "Menggambar", "Menyanyi", "Trending", "Olahraga", "Lainnya", "Tidak ada"]
)

if st.button("Dapatkan Rekomendasi"):

    if minat in ["Matematika", "Fisika", "Kimia"] and nilai == "Tinggi":
        st.success("Kamu cocok dengan Jurusan Saintek")

    elif minat in ["Sosial", "Bahasa", "Bisnis"] and nilai in ["Tinggi", "Sedang"]:
        st.success("Kamu cocok dengan Jurusan Soshum")

    elif minat == "Seni" or hobi in ["Menggambar", "Menyanyi"]:
        st.success("Kamu cocok dengan Jurusan Seni / Desain")

    elif minat == "Teknologi" and hobi == "Trending":
        st.success("Kamu cocok dengan Jurusan Teknologi Informasi")

    elif minat == "Olahraga" or hobi == "Olahraga":
        st.success("Kamu cocok dengan Jurusan Olahraga")

    else:
        st.warning("Rekomendasi belum tersedia")
        
