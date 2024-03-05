import streamlit as st
from PIL import Image

# Judul
st.title("Analisis Data Dicoding")

# Pertanyaan 1
st.header(
    "Pertanyaan 1 : Apakah ada perbedaan dalam jumlah peminjaman sepeda pada hari libur dibandingkan dengan hari biasa?"
)
st.write(
    "Dari hasil analisis, terlihat bahwa jumlah peminjaman sepeda pada hari biasa (non-holiday) lebih tinggi dibandingkan dengan hari libur (holiday). Hal ini menunjukkan bahwa mayoritas peminjaman sepeda terjadi pada hari-hari biasa, yang mungkin disebabkan oleh aktivitas sehari-hari seperti pergi ke tempat kerja atau sekolah. Oleh karena itu, dapat disimpulkan bahwa hari biasa cenderung menjadi periode di mana peminjaman sepeda paling banyak terjadi"
)

# Gambar 1
image1 = Image.open("pertanyaan 1.png")
st.image(image1, caption="Deskripsi Gambar 1", use_column_width=True)

# Pertanyaan 2
st.header("Pertanyaan 2")
st.write("Ini adalah pertanyaan kedua.")

# Gambar 2
st.subheader("Gambar 2")
image2 = Image.open("2.png")
st.image(image2, caption="Deskripsi Gambar 2", use_column_width=True)

# Pertanyaan 3
st.header("Pertanyaan 3")
st.write("Ini adalah pertanyaan ketiga.")

# Gambar 3
st.subheader("Gambar 3")
image3 = Image.open("3.png")
st.image(image3, caption="Deskripsi Gambar 3", use_column_width=True)
