import streamlit as st
from PIL import Image

# Judul
st.title("Analisis Data dengan Streamlit")

# Pertanyaan 1
st.header("Pertanyaan 1")
st.write("Ini adalah pertanyaan pertama.")

# Gambar 1
st.subheader("Gambar 1")
image1 = Image.open("gambar1.png")
st.image(image1, caption="Deskripsi Gambar 1", use_column_width=True)

# Pertanyaan 2
st.header("Pertanyaan 2")
st.write("Ini adalah pertanyaan kedua.")

# Gambar 2
st.subheader("Gambar 2")
image2 = Image.open("gambar2.png")
st.image(image2, caption="Deskripsi Gambar 2", use_column_width=True)

# Pertanyaan 3
st.header("Pertanyaan 3")
st.write("Ini adalah pertanyaan ketiga.")

# Gambar 3
st.subheader("Gambar 3")
image3 = Image.open("gambar3.png")
st.image(image3, caption="Deskripsi Gambar 3", use_column_width=True)
